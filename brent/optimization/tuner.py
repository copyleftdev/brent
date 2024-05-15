from scipy.optimize import minimize

class Tuner:
    def __init__(self, objective_function, initial_guess, bounds=None, constraints=None):
        """
        Initialize the Tuner with the objective function and optimization parameters.

        :param objective_function: The function to minimize.
        :param initial_guess: The initial guess for the parameters.
        :param bounds: The bounds for the parameters.
        :param constraints: The constraints for the optimization.
        """
        self.objective_function = objective_function
        self.initial_guess = initial_guess
        self.bounds = bounds
        self.constraints = constraints
        self.result = None

    def tune(self, method='L-BFGS-B', options=None):
        """
        Perform the optimization.

        :param method: The optimization method to use (default: 'L-BFGS-B').
        :param options: Additional options to pass to the optimizer.
        :return: The result of the optimization.
        """
        self.result = minimize(
            self.objective_function,
            self.initial_guess,
            method=method,
            bounds=self.bounds,
            constraints=self.constraints,
            options=options
        )
        return self.result

    def get_optimized_parameters(self):
        """
        Get the optimized parameters.

        :return: The optimized parameters if the optimization was successful, otherwise None.
        """
        if self.result and self.result.success:
            return self.result.x
        return None

    def get_optimization_result(self):
        """
        Get the full optimization result.

        :return: The full result of the optimization.
        """
        return self.result

