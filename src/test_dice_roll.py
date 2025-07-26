import unittest
from unittest.mock import patch
import random

from dice_rolling import roll_dice 

class TestRollDice(unittest.TestCase):
    @patch('random.randint')
    def test_standard_roll(self, mock_randint):
        """Test a standard roll like 2d6+3."""
        mock_randint.side_effect = [4, 6]  # Simulate rolling 4 and 6
        result = roll_dice(2, 6, 3)
        self.assertEqual(result, 13)  # 4 + 6 + 3 = 13

    @patch('random.randint')
    def test_single_die_no_modifier(self, mock_randint):
        """Test rolling a single die with no modifier."""
        mock_randint.side_effect = [5]
        result = roll_dice(1, 20, 0)
        self.assertEqual(result, 5)

    @patch('random.randint')
    def test_zero_dice(self, mock_randint):
        """Test rolling zero dice with a modifier."""
        result = roll_dice(0, 6, 5)
        self.assertEqual(result, 5)  # Only modifier applies

    @patch('random.randint')
    def test_negative_modifier(self, mock_randint):
        """Test rolling with a negative modifier."""
        mock_randint.side_effect = [3, 2]
        result = roll_dice(2, 4, -1)
        self.assertEqual(result, 4)  # 3 + 2 - 1 = 4

    def test_invalid_num_dice(self):
        """Test negative number of dice raises ValueError."""
        with self.assertRaises(ValueError):
            roll_dice(-1, 6, 0)

    def test_invalid_num_sides(self):
        """Test non-positive number of sides raises ValueError."""
        with self.assertRaises(ValueError):
            roll_dice(2, 0, 0)
        with self.assertRaises(ValueError):
            roll_dice(2, -1, 0)

    @patch('random.randint')
    def test_roll_within_bounds(self, mock_randint):
        """Test rolls are within expected bounds."""
        mock_randint.side_effect = [1, 6, 3]
        result = roll_dice(3, 6, 2)
        self.assertTrue(5 <= result <= 20)  # Min: 1+1+1+2=5, Max: 6+6+6+2=20

if __name__ == '__main__':
    unittest.main()