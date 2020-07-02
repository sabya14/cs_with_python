from unittest import TestCase

from dynamic_programming.partition_labels import partition_labels


class PartitionTest(TestCase):
    def test_partition_labels(self):
        labels = partition_labels("ababcbacadefegdehijhklij")
        self.assertListEqual([9,7,8], labels)

    def test_partition_single_char(self):
        labels = partition_labels("eaaaabaaec")
        self.assertListEqual([9,1], labels)