"""
Problem Statement - https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


class FrequencyQueries:
    state = None

    def __init__(self):
        self.state = {}

    def operation(self, operation_code, operation_value):
        if operation_code == 1:
            if operation_value in self.state:
                self.state[operation_value] += 1
            else:
                self.state[operation_value] = 1
        if operation_code == 2:
            if operation_value in self.state:
                if self.state[operation_value] == 1:
                    self.state.pop(operation_value)
                else:
                    self.state[operation_value] -= 1
        if operation_code == 3:
            for key, value in self.state.items():
                if value == operation_value:
                    return key
            return 0

    def get_state(self):
        return self.state


if "__name__" == "__main__":
    n = int(input())
    data = []
    fq = FrequencyQueries()
    for i in range(0, n):
        operation_code, operation_value = map(int, input().split())
        fq.operation(operation_code, operation_value)
