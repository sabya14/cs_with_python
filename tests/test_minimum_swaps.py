from unittest import TestCase

from arrays.minimum_swaps import minimum_swaps


class Test(TestCase):
    def test_minimum_swaps(self):
        input = [2, 1, 5, 4, 3]
        swaps = minimum_swaps(input)
        self.assertEqual(swaps, 2)

    def test_minimum_swaps_case_1(self):
        input = [4, 3, 1, 2]
        swaps = minimum_swaps(input)
        self.assertEqual(swaps, 3)