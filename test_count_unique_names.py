import unittest

from main import countUniqueNames


class TestCountUniqueNames(unittest.TestCase):
    def test_exact_match(self):
        result = countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")
        self.assertEqual(result, 1)

    def test_partial_match(self):
        result = countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")
        self.assertEqual(result, 1)

    def test_nickname_match(self):
        result = countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli")
        self.assertEqual(result, 1)

    def test_last_name_first(self):
        result = countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah")
        self.assertEqual(result, 1)

    def test_no_significant_similarity(self):
        result = countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli")
        self.assertEqual(result, 2)

    def test_case_insensitivity(self):
        result = countUniqueNames("John", "Doe", "john", "Doe", "John Doe")
        self.assertEqual(result, 1)

    def test_middle_name_match(self):
        result = countUniqueNames("Alice Ann", "Smith", "Alice", "Smith", "Alice Ann Smith")
        self.assertEqual(result, 1)

    def test_last_name_first_with_typo(self):
        result = countUniqueNames("John", "Doe", "Jane", "Doe", "Doe John")
        self.assertEqual(result, 2)

    def test_different_last_names(self):
        result = countUniqueNames("John", "Doe", "Jane", "Smith", "John Smith")
        self.assertEqual(result, 3)

    def test_none_values(self):
        with self.assertRaises(ValueError):
            countUniqueNames(None, "Doe", "Jane", "Smith", "John Smith")

    def test_last_name_first_with_multiple_spaces(self):
        result = countUniqueNames("John", "Doe", "Jane", "Smith", "Smith  Jane")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()

