import unittest
from unittest.mock import patch, MagicMock
from brent.binary_execution.executor import BinaryExecutor
import subprocess
import tempfile
import os

class TestBinaryExecutor(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.binary_path = os.path.join(self.temp_dir.name, 'binary')
        with open(self.binary_path, 'w') as f:
            f.write("#!/bin/bash\necho 'Binary executed'")
        os.chmod(self.binary_path, 0o755)

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch('subprocess.run')
    def test_execute_success(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Execution successful", returncode=0)
        binary_executor = BinaryExecutor(self.binary_path)

        output = binary_executor.execute()
        self.assertEqual(output, "Execution successful")
        mock_run.assert_called_once_with([self.binary_path], check=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_execute_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, self.binary_path, output="Execution failed")
        binary_executor = BinaryExecutor(self.binary_path)

        output = binary_executor.execute()
        self.assertEqual(output, "Execution failed")
        mock_run.assert_called_once_with([self.binary_path], check=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_execute_with_args_success(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Execution with args successful", returncode=0)
        binary_executor = BinaryExecutor(self.binary_path)

        output = binary_executor.execute_with_args(['--arg1', 'value1'])
        self.assertEqual(output, "Execution with args successful")
        mock_run.assert_called_once_with([self.binary_path, '--arg1', 'value1'], check=True, capture_output=True, text=True)

    @patch('subprocess.Popen')
    def test_execute_in_background_success(self, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout.read.return_value = "Background execution successful"
        mock_popen.return_value = mock_process
        binary_executor = BinaryExecutor(self.binary_path)

        process = binary_executor.execute_in_background()
        self.assertIsNotNone(process)
        self.assertEqual(process.stdout.read(), "Background execution successful")
        mock_popen.assert_called_once_with([self.binary_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    @patch('subprocess.run')
    def test_execute_with_env_success(self, mock_run):
        mock_run.return_value = MagicMock(stdout="Execution with env successful", returncode=0)
        binary_executor = BinaryExecutor(self.binary_path)

        output = binary_executor.execute_with_env({'ENV_VAR': 'value'})
        self.assertEqual(output, "Execution with env successful")
        expected_env = os.environ.copy()
        expected_env.update({'ENV_VAR': 'value'})
        mock_run.assert_called_once_with([self.binary_path], check=True, capture_output=True, text=True, env=expected_env)

if __name__ == '__main__':
    unittest.main()
