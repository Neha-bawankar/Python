def reverse_generator(data):
    """A generator function to yield items from a sequence in reverse order."""
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

def fibonacci_generator(max_count):
    """A generator function to yield a Fibonacci sequence up to max_count numbers."""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

def prime_generator(limit):
    """A generator function to yield prime numbers up to a specified limit."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    number = 2
    while number < limit:
        if is_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
    # Using the reverse_generator
    data = [1, 2, 3, 4, 5]
    print("Reversed Data:")
    for item in reverse_generator(data):
        print(item)

    print("\n")

    # Using the fibonacci_generator
    max_count = 10
    print(f"First {max_count} Fibonacci numbers:")
    for number in fibonacci_generator(max_count):
        print(number)

    print("\n")

    # Using the prime_generator
    limit = 30
    print(f"Prime numbers up to {limit}:")
    for prime in prime_generator(limit):
        print(prime)