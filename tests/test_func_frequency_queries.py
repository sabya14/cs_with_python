from unittest import TestCase

from dictonaries.func_frequency_queries import freq_query


class Test(TestCase):
    def test_freq_query(self):
        queries = [
            [1, 1],
            [1, 1],
            [1, 1],
            [3, 3],
        ]
        output = freq_query(queries)
        self.assertListEqual([1], output)

        queries = [
            [1, 3],
            [2, 3],
            [3, 2],
            [1, 4],
            [1, 5],
            [1, 5],
            [1, 4],
            [3, 2],
            [2, 4],
            [3, 2],
        ]
        output = freq_query(queries)
        self.assertListEqual(output, [0, 1, 1])
