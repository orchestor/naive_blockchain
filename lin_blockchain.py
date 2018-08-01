class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
    def add_new_block(self):
        """ Add a new block and return the new chain

        """
        pass
    def new_transaction(self, sender, recipient, amount):
        """ Return the index of the block which holds the transaction
            Adds a new transaction to the list
        """
        self.current_transaction.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )

        return self.last_block['index'] + 1
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
