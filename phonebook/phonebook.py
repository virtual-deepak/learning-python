class Phonebook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    """A phonebook is said to be consistent if no number is a prefix of another number."""

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if (name1 != name2) and number1.startswith(number2):
                    return False
        return True
