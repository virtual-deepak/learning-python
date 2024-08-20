import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def setUp(self) -> None:
        """Runs before every test case"""
        self.phonebook = Phonebook()

    def tearDown(self) -> None:
        """Runs after every test case (even if the test case failed)"""
        pass

    def test_lookup_by_name(self):
        # Arrange
        self.phonebook.add("Bob", "12345")
        # Act
        number = self.phonebook.lookup("Bob")
        # Assert
        self.assertEqual(number, "12345")

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "67890")
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")
        is_consistent = self.phonebook.is_consistent()
        self.assertFalse(is_consistent)

    def test_is_inconsistent_with_prefix_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")
        is_consistent = self.phonebook.is_consistent()
        self.assertFalse(is_consistent)
