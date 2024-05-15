import unittest
from brent.binary_execution.executor import BinaryExecutor

class TestBinaryExecutor(unittest.TestCase):
    def test_execute(self):
        executor = BinaryExecutor('/path/to/binary')
        result = executor.execute()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
