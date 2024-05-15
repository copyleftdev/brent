import os
import subprocess

class BinaryExecutor:
    def __init__(self, binary_path):
        """
        Initialize the BinaryExecutor with the path to the binary file.

        :param binary_path: Path to the binary file to be executed.
        """
        if not os.path.isfile(binary_path):
            raise FileNotFoundError(f"The binary file '{binary_path}' does not exist.")
        self.binary_path = binary_path

    def execute(self):
        """
        Execute the binary file.

        :return: The output of the binary execution.
        """
        try:
            result = subprocess.run([self.binary_path], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Execution failed: {e}")
            return e.output

    def execute_with_args(self, args):
        """
        Execute the binary file with additional arguments.

        :param args: List of arguments to pass to the binary.
        :return: The output of the binary execution.
        """
        try:
            result = subprocess.run([self.binary_path] + args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Execution failed: {e}")
            return e.output

    def execute_in_background(self):
        """
        Execute the binary file in the background.

        :return: The Popen object representing the background process.
        """
        try:
            process = subprocess.Popen([self.binary_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return process
        except Exception as e:
            print(f"Failed to execute in background: {e}")
            return None

    def execute_with_env(self, env_vars):
        """
        Execute the binary file with additional environment variables.

        :param env_vars: Dictionary of environment variables to set for the binary execution.
        :return: The output of the binary execution.
        """
        try:
            env = os.environ.copy()
            env.update(env_vars)
            result = subprocess.run([self.binary_path], check=True, capture_output=True, text=True, env=env)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Execution failed: {e}")
            return e.output
