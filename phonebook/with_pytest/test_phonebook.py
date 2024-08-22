from phonebook.phonebook import Phonebook

import pytest


@pytest.fixture
def phonebook():
    return Phonebook()


def test_lookup_by_name(phonebook):
    # Arrange
    phonebook.add("Bob", "12345")
    # Act
    number = phonebook.lookup("Bob")
    # Assert
    assert number == "12345"


def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")


def test_empty_phonebook_is_consistent(phonebook):
    is_consistent = phonebook.is_consistent()
    assert is_consistent == True


@pytest.mark.parametrize(
    "entry1, entry2, expected_is_consistent",
    [
        (("Bob", "12345"), ("Sue", "67890"), True),
        (("Bob", "12345"), ("Sue", "12345"), False),
        (("Bob", "12345"), ("Sue", "123"), False),
    ], 
    ids=["Distinct Values", "Same Values", "Same Prefix"]
)
def test_is_consistent(phonebook, entry1, entry2, expected_is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    actual_is_consistent = phonebook.is_consistent()
    assert actual_is_consistent == expected_is_consistent

@pytest.mark.skip("Work in progress")
def test_phonebook_new_feature():
    assert False