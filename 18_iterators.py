class ListIterator:
    def __init__(self, data):
        self.data = data        
        self.index = 0          

    def __iter__(self):
        return self             

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration # no more items
        value = self.data[self.index]
        self.index += 1
        return value


# Using the custom iterator
numbers = [10, 20, 30, 40, 50]
iterator = ListIterator(numbers)

for num in iterator:
    print(num)
