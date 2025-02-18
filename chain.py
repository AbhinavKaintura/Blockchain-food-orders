from time import time
from block import Block


class FoodChain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the chain.
        """
        genesis_block = Block(0, [], time(), "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_order(self, customer, restaurant, items, total_amount):
        """
        Add a new food order to pending transactions.
        """
        order = {
            'timestamp': time(),
            'customer': customer,
            'restaurant': restaurant,
            'items': items,
            'total_amount': total_amount,
            'status': 'pending'
        }
        self.pending_transactions.append(order)
        return self.get_last_block().index + 1

    def mine_pending_orders(self):
        """
        Create a new block with pending transactions and add it to the chain.
        """
        if not self.pending_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.pending_transactions,
            timestamp=time(),
            previous_hash=last_block.hash
        )

        # Simple proof of work
        while not new_block.hash.startswith('000'):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block
