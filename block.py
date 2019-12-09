class Block:
    """
    Class that holds information about a block.
    """

    def __init__(self, utxo, timestamp):
        """
        :param utxo: int
        utxo describes the address of the stake that minted the block
        :param timestamp: float
        timestamp describes the time of the minting of the block
        :param flag: bool
        a boolean to describe whether a block was minted under conditions where the attacker had multiple stakes winning
        at the same time and the honest minters had none.
        """
        self.utxo = utxo
        self.timestamp = timestamp
        self.flag = False
