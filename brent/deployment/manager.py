import os
import subprocess

class DeploymentManager:
    def __init__(self, deployment_script_path):
        """
        Initialize the DeploymentManager with the path to the deployment script.

        :param deployment_script_path: Path to the deployment script to be executed.
        """
        if not os.path.isfile(deployment_script_path):
            raise FileNotFoundError(f"The deployment script '{deployment_script_path}' does not exist.")
        self.deployment_script_path = deployment_script_path

    def deploy(self, environment):
        """
        Execute the deployment script for the specified environment.

        :param environment: The deployment environment (e.g., 'staging', 'production').
        :return: The output of the deployment script execution.
        """
        try:
            env_vars = os.environ.copy()
            env_vars['DEPLOY_ENV'] = environment
            result = subprocess.run([self.deployment_script_path], check=True, capture_output=True, text=True, env=env_vars)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Deployment failed: {e}")
            return e.output

    def rollback(self, rollback_script_path):
        """
        Execute the rollback script to revert the deployment.

        :param rollback_script_path: Path to the rollback script to be executed.
        :return: The output of the rollback script execution.
        """
        if not os.path.isfile(rollback_script_path):
            raise FileNotFoundError(f"The rollback script '{rollback_script_path}' does not exist.")
        try:
            result = subprocess.run([rollback_script_path], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Rollback failed: {e}")
            return e.output

    def check_status(self, status_command):
        """
        Check the status of the deployed application.

        :param status_command: Command to check the status of the deployment.
        :return: The output of the status command execution.
        """
        try:
            result = subprocess.run(status_command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Status check failed: {e}")
            return e.output

