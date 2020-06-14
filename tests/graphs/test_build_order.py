from unittest import TestCase

from graphs.build_order import BuildOrder


class TestBuildOrder(TestCase):

    def test_given_a_list_pair_should_return_build_order_if_exists(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
        expected_order = ['f', 'e', 'a', 'b', 'd', 'c']
        order = BuildOrder(projects);
        actual_order = order.get_order(dependencies)
        self.assertListEqual(sorted(actual_order), sorted(expected_order))

