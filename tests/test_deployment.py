import unittest
from unittest.mock import patch, MagicMock
import os
import subprocess
import tempfile
from brent.deployment.manager import DeploymentManager

class TestDeploymentManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.deployment_script = os.path.join(self.temp_dir.name, 'deploy.sh')
        with open(self.deployment_script, 'w') as f:
            f.write("#!/bin/bash\necho 'Deployment script executed'")
        os.chmod(self.deployment_script, 0o755)

        self.rollback_script = os.path.join(self.temp_dir.name, 'rollback.sh')
        with open(self.rollback_script, 'w') as f:
            f.write("#!/bin/bash\necho 'Rollback script executed'")
        os.chmod(self.rollback_script, 0o755)

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch('os.path.isfile', return_value=True)
    def test_init_deployment_script_not_found(self, mock_isfile):
        mock_isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            DeploymentManager('/invalid/path/to/deploy.sh')

    @patch('os.path.isfile', return_value=True)
    @patch('subprocess.run')
    def test_deploy_success(self, mock_run, mock_isfile):
        mock_run.return_value = MagicMock(stdout="Deployment successful", returncode=0)
        deployment_manager = DeploymentManager(self.deployment_script)

        output = deployment_manager.deploy('staging')
        self.assertEqual(output, "Deployment successful")
        mock_run.assert_called_once_with([self.deployment_script], check=True, capture_output=True, text=True, env=unittest.mock.ANY)

    @patch('os.path.isfile', return_value=True)
    @patch('subprocess.run')
    def test_deploy_failure(self, mock_run, mock_isfile):
        mock_run.side_effect = subprocess.CalledProcessError(1, self.deployment_script, output="Deployment failed")
        deployment_manager = DeploymentManager(self.deployment_script)

        output = deployment_manager.deploy('staging')
        self.assertEqual(output, "Deployment failed")
        mock_run.assert_called_once_with([self.deployment_script], check=True, capture_output=True, text=True, env=unittest.mock.ANY)

    @patch('os.path.isfile', return_value=True)
    def test_init_rollback_script_not_found(self, mock_isfile):
        mock_isfile.side_effect = lambda path: path == self.deployment_script
        deployment_manager = DeploymentManager(self.deployment_script)
        with self.assertRaises(FileNotFoundError):
            deployment_manager.rollback('/invalid/path/to/rollback.sh')

    @patch('os.path.isfile', return_value=True)
    @patch('subprocess.run')
    def test_rollback_success(self, mock_run, mock_isfile):
        mock_run.return_value = MagicMock(stdout="Rollback successful", returncode=0)
        deployment_manager = DeploymentManager(self.deployment_script)

        rollback_output = deployment_manager.rollback(self.rollback_script)
        self.assertEqual(rollback_output, "Rollback successful")
        mock_run.assert_called_once_with([self.rollback_script], check=True, capture_output=True, text=True)

    @patch('os.path.isfile', return_value=True)
    @patch('subprocess.run')
    def test_rollback_failure(self, mock_run, mock_isfile):
        mock_run.side_effect = subprocess.CalledProcessError(1, self.rollback_script, output="Rollback failed")
        deployment_manager = DeploymentManager(self.deployment_script)

        rollback_output = deployment_manager.rollback(self.rollback_script)
        self.assertEqual(rollback_output, "Rollback failed")
        mock_run.assert_called_once_with([self.rollback_script], check=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_check_status_success(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Service is running", returncode=0)
        deployment_manager = DeploymentManager(self.deployment_script)

        status_output = deployment_manager.check_status("systemctl status myapp")
        self.assertEqual(status_output, "Service is running")
        mock_run.assert_called_once_with("systemctl status myapp", shell=True, check=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_check_status_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, 'systemctl status myapp', output="Service is not running")
        deployment_manager = DeploymentManager(self.deployment_script)

        status_output = deployment_manager.check_status("systemctl status myapp")
        self.assertEqual(status_output, "Service is not running")
        mock_run.assert_called_once_with("systemctl status myapp", shell=True, check=True, capture_output=True, text=True)

if __name__ == '__main__':
    unittest.main()
