import unittest
from math_quiz import get_random_integer, get_random_operator, generate_math_problem

class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if the random operator is one of the expected values
        operators = {'+', '-', '*'}
        for _ in range(1000):
            operator = get_random_operator()
            self.assertIn(operator, operators)

    def test_generate_math_problem(self):
        # Test cases to verify correct problem generation and answer calculation
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 5, '*', '4 * 5', 20),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
