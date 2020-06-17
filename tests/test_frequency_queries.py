from unittest import TestCase

from dictonaries.frequency_queries import FrequencyQueries


class TestFrequencyQueries(TestCase):

    def testShouldInsertToArrayOnAddOperation(self):
        fq = FrequencyQueries()
        fq.operation(1, 1)
        state = fq.get_state()
        self.assertDictEqual(state, {1: 1})

        fq.operation(1, 2)
        state = fq.get_state()
        self.assertDictEqual(state, {1: 1, 2: 1})

    def testShouldDeleteAnElementIfPresent(self):
        fq = FrequencyQueries()
        fq.operation(1, 1)
        fq.operation(1, 1)
        fq.operation(2, 1)
        fq.operation(2, 3)
        state = fq.get_state()
        self.assertDictEqual(state, {1: 1})

    def testShouldReturn1IfAnIntegerIsPresentWhoseFrequencyMatchesInputForType3Operation(self):
        fq = FrequencyQueries()
        fq.operation(1, 1)
        fq.operation(1, 1)
        fq.operation(1, 1)
        output = fq.operation(3, 3)
        self.assertEqual(output, 1)

    def testShouldReturn0IfAnIntegerIsPresentWhoseFrequencyMatchesInputForType3Operation(self):
        fq = FrequencyQueries()
        fq.operation(1, 1)
        fq.operation(1, 1)
        fq.operation(1, 1)
        output = fq.operation(3, 2)
        self.assertEqual(output, 0)
