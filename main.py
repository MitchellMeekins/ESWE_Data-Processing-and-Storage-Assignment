class InMemoryDB:
    transaction_active = False
    memory_dict = {}
    old_memory_dict = {}

    def get(self, key: str):
        return self.old_memory_dict.get(key)

    def put(self, key: str, val: int):
        if self.transaction_active is False:
            raise Exception("Transaction not active.")
        self.memory_dict[key] = val

    def begin_transaction(self):
        self.transaction_active = True

    def commit(self):
        if self.transaction_active is False:
            raise Exception("Transaction not active.")
        self.old_memory_dict = self.memory_dict
        self.transaction_active = False

    def rollback(self):
        if self.transaction_active is False:
            raise Exception("Transaction not active.")
        self.memory_dict = self.old_memory_dict
        self.transaction_active = False


if __name__ == '__main__':
    inmemoryDB = InMemoryDB()




