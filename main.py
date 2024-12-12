class InMemoryDB:
    def __init__(self):
        self.transaction_active = False
        self.committed_dict = {}
        self.transaction_dict = {}

    def get(self, key: str):
        return self.committed_dict.get(key)

    def put(self, key: str, val: int):
        if not self.transaction_active:
            raise Exception("Transaction not active.")
        self.transaction_dict[key] = val

    def begin_transaction(self):
        if self.transaction_active:
            raise Exception("Transaction already active.")  # This wasn't demonstrated in Figure 2 but was in the
            # instructions
        self.transaction_active = True
        self.transaction_dict = {}

    def commit(self):
        if not self.transaction_active:
            raise Exception("Transaction not active.")
        self.committed_dict.update(self.transaction_dict)
        self.transaction_active = False
        self.transaction_dict = {}

    def rollback(self):
        if not self.transaction_active:
            raise Exception("Transaction not active.")
        self.transaction_active = False
        self.transaction_dict = {}
