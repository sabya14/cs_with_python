class TestIterator:
    def __init__(self, _list):
        self.list = _list

    def __iter__(self):
        return self

    def __next__(self):
        if self.list:
            # pop(0) pops from start
            return self.list.pop(0)
        else:
            raise StopIteration


for i in TestIterator([1,2,3,4,5]):
    print(i)
