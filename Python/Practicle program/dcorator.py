import time
import functools

def execution_time_decorator(func):
    """Decorator to measure the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def sample_function(x, y):
    """Sample function to demonstrate the decorator."""
    time.sleep(1)  # Simulate a time-consuming operation
    return x + y

if __name__ == "__main__":
    result = sample_function(5, 10)
    print(f"Result: {result}")