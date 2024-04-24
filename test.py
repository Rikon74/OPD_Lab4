import unittest
from main import total_amount, interest_rate, starting_capital, deposit_term


class TestSite(unittest.TestCase):

    def test_float(self):
        self.assertEqual(type(total_amount(200000, 13, 10)), float)
        self.assertEqual(type(interest_rate(700000, 200000, 10)), float)
        self.assertEqual(type(starting_capital(700000, 13, 10)), float)
        self.assertEqual(type(deposit_term(700000, 200000, 13)), float)


if __name__ == '__main__':
    unittest.main()
