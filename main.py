import hashlib
import time
import random
from block import Block
from stake import Stake

"""
A simulation of a proof of stake blockchain network using the timestamp and utxo (address of previous winning stake) as kernel.
The simulation aims to show the improvement of cooperation between stakeowners in a low trust required relationsship
and the increased minted blocks a cooperation will yield.
"""


class Run:
    def __init__(self):
        self.myStake = []  # List of stakes that are "owned"
        self.otherStakes = []  # List of stakes that are controlled by others
        self.blocks = []  # List of blocks that have been minted
        self.target = 2 ** 256 / 4  # The target minting is trying to reach. The
        self.blocks.append(
            Block(-1, time.time()))  # Add a genesis block, the address -1 is arbitrary and does not matter
        self.winnings = 0 # Counter for times that the block is being minted by a stake in myStake
        self.multipleOwnWinners = 0  # Counter for times there are multiple winners and all of them are in myStake
        self.otherSplits = 4 # Definition of the amount splits that the other stakes have

    def main(self):
        """
        Setup function where the parameters of the simulation is being chosen, and the simulation is initiated
        :return: None
        """
        stakeInPercent = float(input("Give the stake in percent of total stake: ")) / 100
        amountOfCoins = int(input("Give the amount of splits for the stake: "))
        blockToBeStaked = int(input("Give amount of blocks to be minted: "))
        self.myStake = [Stake(stakeInPercent / amountOfCoins) for i in range(amountOfCoins)]
        self.otherStakes = [Stake((1 - stakeInPercent) / self.otherSplits) for i in
                            range(self.otherSplits)]  # Note that all the other stakes will have an equal stake amount
        self.mintCoins(blockToBeStaked)

    def mintCoins(self, amountOfBlocks):
        """
        Function that generates new blocks according to all stakes that appears myStake and otherStakes
        :param amountOfBlocks: int
        :return: None
        """
        for i in range(amountOfBlocks):
            winnerStakes, timeStamp = self.getNextWinner()
            if all(stake in self.myStake for stake in
                   winnerStakes):  # Checks if all the winners of the current block are part of myStake. Often there is only one winner
                self.winnings += 1

                if len(winnerStakes) > 1:  # If all winners are in myStake and there are multiple winners
                    """
                    Go through all of the winnerstakes, and find out which stake that will secure the lowest time until
                    one of the stakes in myStake wins the preceding block
                    """
                    self.multipleOwnWinners += 1
                    smallestTime = None
                    bestStake = None
                    for stake in winnerStakes:
                        stakeTime = min(
                            [self.getNextWinTime(myNextStake, Block(stake.address, timeStamp)) for myNextStake in
                             self.myStake])

                        if smallestTime == None or smallestTime > stakeTime:
                            bestStake = stake
                            smallestTime = stakeTime
                else:
                    bestStake = winnerStakes[0]

                # bestStake = random.choice(winnerStakes)
                # print("All winners are ours")
                self.blocks.append(Block(bestStake.address, timeStamp))
            else:
                bestStake = random.choice(winnerStakes)
                self.blocks.append(Block(bestStake.address, timeStamp))
                if bestStake in self.myStake:
                    self.winnings += 1

    def getNextWinTime(self, stake, block):
        """
        Function that computes when a single stake, given a block, will be able to mint its next block
        :param stake: float
        :param block: Block
        :return: int
        """
        rounds = 0
        while True:
            rounds += 1
            if int(self.getHash(block, stake.address, block.timestamp + 16 * rounds), 16) < self.target * stake.stake:
                return rounds

    def getNextWinner(self):
        """
        Function that returns the next winners
        :return: [Stake], float
        """
        lastTime = self.blocks[-1].timestamp
        winnerFound = False
        winners = []
        rounds = 0
        while not winnerFound:
            rounds += 1
            for stake in self.myStake:
                if int(self.getHash(self.blocks[-1], stake.address, lastTime + 16 * rounds),
                       16) < self.target * stake.stake:
                    winners.append(stake)
                    winnerFound = True
            for stake in self.otherStakes:
                if int(self.getHash(self.blocks[-1], stake.address, lastTime + 16 * rounds),
                       16) < self.target * stake.stake:
                    winners.append(stake)
                    winnerFound = True
        return winners, lastTime + 16 * rounds

    def getHash(self, block, address, timestamp):
        """
        Returns a string of the hexadecimal hash using sha256
        :param block: Block
        :param address: int
        :param timestamp: float
        :return: str
        """
        return hashlib.sha256(
            (str(block.timestamp) + str(block.utxo) + str(address) + str(timestamp)).encode('utf-8')).hexdigest()


if __name__ == "__main__":
    run = Run()
    run.main()
    print(run.winnings)
    print(run.multipleOwnWinners)
