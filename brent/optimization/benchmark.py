import time
import statistics
from functools import wraps

class Benchmark:
    def __init__(self):
        """
        Initialize the Benchmark class with an empty results list.
        """
        self.results = []

    def time_function(self, func, *args, **kwargs):
        """
        Time the execution of a function.

        :param func: The function to time.
        :param args: Positional arguments to pass to the function.
        :param kwargs: Keyword arguments to pass to the function.
        :return: The result of the function execution.
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.results.append(elapsed_time)
        return result

    def benchmark(self, func):
        """
        Decorator to benchmark a function.

        :param func: The function to benchmark.
        :return: The decorated function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            return self.time_function(func, *args, **kwargs)
        return wrapper

    def report(self):
        """
        Print a report of the benchmark results.
        """
        if not self.results:
            print("No benchmark results to report.")
            return

        mean_time = statistics.mean(self.results)
        median_time = statistics.median(self.results)
        stdev_time = statistics.stdev(self.results) if len(self.results) > 1 else 0.0
        min_time = min(self.results)
        max_time = max(self.results)

        print(f"Benchmark Report:")
        print(f"  Mean Time: {mean_time:.6f} seconds")
        print(f"  Median Time: {median_time:.6f} seconds")
        print(f"  Standard Deviation: {stdev_time:.6f} seconds")
        print(f"  Min Time: {min_time:.6f} seconds")
        print(f"  Max Time: {max_time:.6f} seconds")

    def clear_results(self):
        """
        Clear the benchmark results.
        """
        self.results.clear()

