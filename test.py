import unittest
from main import InMemoryDB


class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        self.inmemoryDB = InMemoryDB()

    def test_initial_get(self):
        self.assertIsNone(self.inmemoryDB.get("A"))

    def test_put_without_transaction(self):
        with self.assertRaises(Exception):
            self.inmemoryDB.put("A", 5)

    def test_transaction_commit(self):
        self.inmemoryDB.begin_transaction()
        self.inmemoryDB.put("A", 5)
        self.assertIsNone(self.inmemoryDB.get("A"))

        self.inmemoryDB.put("A", 6)
        self.inmemoryDB.commit()

        self.assertEqual(self.inmemoryDB.get("A"), 6)

    def test_commit_without_transaction(self):
        with self.assertRaises(Exception):
            self.inmemoryDB.commit()

    def test_rollback_without_transaction(self):
        with self.assertRaises(Exception):
            self.inmemoryDB.rollback()

    def test_transaction_rollback(self):
        self.inmemoryDB.begin_transaction()
        self.inmemoryDB.put("B", 10)
        self.inmemoryDB.rollback()

        self.assertIsNone(self.inmemoryDB.get("B"))

    def test_get_bad_key(self):
        self.assertIsNone(self.inmemoryDB.get("B"))


if __name__ == "__main__":
    unittest.main()
