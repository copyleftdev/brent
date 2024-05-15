# Optimization

The `brent.optimization` package provides tools and utilities for benchmarking, profiling, and tuning applications. This package is designed to help developers optimize their code and improve performance.

## Modules

The `brent.optimization` package includes the following modules:

- `benchmark.py`: Provides functionality to benchmark the execution time of functions.
- `profiler.py`: Provides functionality to profile the performance of code.
- `tuner.py`: Provides functionality to optimize parameters using various optimization techniques.

## benchmark.py

### Overview

The `benchmark.py` module contains the `Benchmark` class, which is used to benchmark the execution time of functions.

### Benchmark Class

#### Initialization

```python
Benchmark()
```

#### Methods

- `time_function(func: Callable, *args, **kwargs) -> Any`
  - Times the execution of a function.
  - `func`: The function to time.
  - `args`: Positional arguments to pass to the function.
  - `kwargs`: Keyword arguments to pass to the function.
  - Returns the result of the function execution.

- `benchmark(func: Callable) -> Callable`
  - Decorator to benchmark a function.
  - `func`: The function to benchmark.
  - Returns the decorated function.

- `report()`
  - Prints a report of the benchmark results.

- `clear_results()`
  - Clears the benchmark results.

#### Example Usage

```python
from brent.optimization.benchmark import Benchmark

benchmark = Benchmark()

@benchmark.benchmark
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

for _ in range(10):
    example_function(1000000)

benchmark.report()
```

## profiler.py

### Overview

The `profiler.py` module contains the `Profiler` class, which is used to profile the performance of code.

### Profiler Class

#### Initialization

```python
Profiler()
```

#### Methods

- `start()`
  - Starts the profiler.

- `stop()`
  - Stops the profiler.

- `print_stats(sort_by: str = 'cumulative')`
  - Prints the profiling statistics.
  - `sort_by`: The criterion by which to sort the profiling results (default: 'cumulative').

- `save_stats(filename: str, sort_by: str = 'cumulative')`
  - Saves the profiling statistics to a file.
  - `filename`: The name of the file to save the profiling results to.
  - `sort_by`: The criterion by which to sort the profiling results (default: 'cumulative').

#### Example Usage

```python
from brent.optimization.profiler import Profiler

profiler = Profiler()

def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

profiler.start()
example_function(1000000)
profiler.stop()
profiler.print_stats()
profiler.save_stats('profiling_results.txt')
```

## tuner.py

### Overview

The `tuner.py` module contains the `Tuner` class, which is used to optimize parameters using various optimization techniques.

### Tuner Class

#### Initialization

```python
Tuner(objective_function: Callable, initial_guess: list, bounds: list = None, constraints: list = None)
```

- `objective_function`: The function to minimize.
- `initial_guess`: The initial guess for the parameters.
- `bounds`: The bounds for the parameters.
- `constraints`: The constraints for the optimization.

#### Methods

- `tune(method: str = 'L-BFGS-B', options: dict = None) -> OptimizeResult`
  - Performs the optimization.
  - `method`: The optimization method to use (default: 'L-BFGS-B').
  - `options`: Additional options to pass to the optimizer.
  - Returns the result of the optimization.

- `get_optimized_parameters() -> list`
  - Gets the optimized parameters.
  - Returns the optimized parameters if the optimization was successful, otherwise `None`.

- `get_optimization_result() -> OptimizeResult`
  - Gets the full optimization result.
  - Returns the full result of the optimization.

#### Example Usage

```python
from brent.optimization.tuner import Tuner

def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2

initial_guess = [0, 0]
bounds = [(None, None), (None, None)]
tuner = Tuner(objective_function=objective_function, initial_guess=initial_guess, bounds=bounds)

result = tuner.tune()
print("Optimization result:", result)

optimized_parameters = tuner.get_optimized_parameters()
print("Optimized parameters:", optimized_parameters)
```

## Detailed Descriptions

### Benchmark

The `Benchmark` class provides a simple interface for measuring the execution time of functions. It supports both direct function calls and a decorator for easy benchmarking. The results can be printed as a report or cleared for fresh benchmarking.

### Profiler

The `Profiler` class leverages Python's built-in `cProfile` to profile the performance of code. It can start and stop the profiler, print statistics to the console, and save the profiling results to a file for further analysis.

### Tuner

The `Tuner` class uses optimization techniques to find the best parameters for a given objective function. It supports a variety of optimization methods and can handle bounds and constraints on the parameters. The results of the optimization can be accessed and used to fine-tune the performance of applications.

## Notes

- Ensure that the functions you benchmark or profile are properly designed for performance testing.
- The optimization techniques used by the `Tuner` class may vary in efficiency based on the complexity of the objective function and the chosen method.
- The `Profiler` class provides detailed insights into the performance of your code, which can help identify bottlenecks and areas for improvement.
- When using the `Benchmark` class, consider running multiple iterations to get an average execution time for more accurate results.

### Explanation

- **Modules**: Lists the modules included in the `brent.optimization` package.
- **benchmark.py**: Provides an overview and detailed description of the `Benchmark` class, including its initialization, methods, and example usage.
- **profiler.py**: Provides an overview and detailed description of the `Profiler` class, including its initialization, methods, and example usage.
- **tuner.py**: Provides an overview and detailed description of the `Tuner` class, including its initialization, methods, and example usage.
- **Detailed Descriptions**: Elaborates on the functionality and use cases of the `Benchmark`, `Profiler`, and `Tuner` classes.
- **Notes**: Provides additional information and considerations for using the classes in the `brent.optimization` package.