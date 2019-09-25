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
        """
        self.utxo = utxo
        self.timestamp = timestamp


