class ReverseIterator:
    """An iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class FibonacciIterator:
    """An iterator for generating a Fibonacci sequence."""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        a, self.a, self.b = self.a, self.b, self.a + self.b
        return a

if __name__ == "__main__":
    # Using the ReverseIterator
    data = [1, 2, 3, 4, 5]
    reverse_iter = ReverseIterator(data)
    print("Reversed Data:")
    for item in reverse_iter:
        print(item)

    print("\n")

    # Using the FibonacciIterator
    max_count = 10
    fibonacci_iter = FibonacciIterator(max_count)
    print(f"First {max_count} Fibonacci numbers:")
    for number in fibonacci_iter:
        print(number)