import unittest
import os
from db_helper import DBHelper

class TestDBHelper(unittest.TestCase):

    def setUp(self):
        self.db_file = "customers.db"
        self.db = DBHelper(self.db_file)

    def tearDown(self):
        self.db.conn.close()
        os.remove(self.db_file)

    def test_add_user(self):
        """Test that adding a user to the database is successful."""
        self.db.add_user("John", "Doe", "john@mail.com", "01-01-2000", "4444444444")
        cur = self.db.conn.cursor()
        cur.execute("SELECT * FROM customers WHERE email='john@mail.com'")
        user = cur.fetchone()
        self.assertEqual(user[0], "John")
        self.assertEqual(user[1], "Doe")
        self.assertEqual(user[2], "john@mail.com")
        self.assertEqual(user[3], "01-01-2000")
        self.assertEqual(user[4], "4444444444")

    def test_get_user(self):
        """Test that getting a user from the database is successful."""
        self.db.add_user("Slim", "Shady", "slim@mail.com", "01-01-1980", "1231231234")
        user = self.db.get_user("slim@mail.com")
        self.assertEqual(user[0], "Slim")
        self.assertEqual(user[1], "Shady")
        self.assertEqual(user[2], "slim@mail.com")
        self.assertEqual(user[3], "01-01-1980")
        self.assertEqual(user[4], "1231231234")

    def test_update_user(self):
        """Test that updating a user in the database is successful."""
        self.db.add_user("Bob", "Marley", "bob@mail.com", "01-01-1980", "1234567890")
        self.db.update_user("bob@mail.com", "jane@mail.com", "Jane", "Doe", "01-01-1981", "9876543210")
        cur = self.db.conn.cursor()
        cur.execute("SELECT * FROM customers WHERE email='jane@mail.com'")
        user = cur.fetchone()
        self.assertEqual(user[0], "Jane")
        self.assertEqual(user[1], "Doe")
        self.assertEqual(user[2], "jane@mail.com")
        self.assertEqual(user[3], "01-01-1981")
        self.assertEqual(user[4], "9876543210")

    def test_delete_user(self):
        """Test that updating a user in the database is successful."""
        email = "alice@mail.com"
        self.db.add_user("Alice", "Baker", email, "01-01-2003", "123456321")
        self.assertTrue(self.db.is_user_exists(email))
        self.db.delete_user(email)
        self.assertFalse(self.db.is_user_exists(email))

if __name__ == '__main__':
    unittest.main()
