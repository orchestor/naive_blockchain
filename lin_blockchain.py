class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
    def add_new_block(self):
        """ Add a new block and return the new chain

        """
        pass
    def new_transaction(self):
        """ Adds a new transaction to the list
        """
        pass

    @staticmethod
    def hash(block):
        """ Return the hashed value of a block
        """
        pass

    @property
    def last_block(self):
        """ Return the last block of the chain
        """
        pass
