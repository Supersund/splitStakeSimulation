class Stake:
    """
    Class that holds information about a stake
    """
    id = 0
    def __init__(self, stake):
        """
        :param stake: float
        """
        self.stake = stake
        self.address = Stake.id
        Stake.id += 1