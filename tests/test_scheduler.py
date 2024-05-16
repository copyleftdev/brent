# import unittest
# from unittest.mock import patch, MagicMock
# from brent.optimization.profiler import Profiler
# import cProfile
# import pstats
# import io

# class TestProfiler(unittest.TestCase):

#     def setUp(self):
#         self.profiler = Profiler()

#     @patch.object(cProfile.Profile, 'enable')
#     def test_start(self, mock_enable):
#         self.profiler.start()
#         mock_enable.assert_called_once()

#     @patch.object(cProfile.Profile, 'disable')
#     def test_stop(self, mock_disable):
#         self.profiler.stop()
#         mock_disable.assert_called_once()

#     @patch('pstats.Stats')
#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_print_stats(self, mock_stdout, mock_stats):
#         mock_instance = mock_stats.return_value
#         self.profiler.print_stats()
#         mock_instance.sort_stats.assert_called_once_with('cumulative')
#         mock_instance.print_stats.assert_called_once()
#         output = mock_stdout.getvalue()
#         self.assertIn("cumulative", output)

#     @patch('pstats.Stats')
#     @patch('builtins.open', new_callable=unittest.mock.mock_open)
#     def test_save_stats(self, mock_open, mock_stats):
#         mock_instance = mock_stats.return_value
#         filename = 'profiling_results.txt'
#         self.profiler.save_stats(filename)
#         mock_open.assert_called_once_with(filename, 'w')
#         mock_instance.sort_stats.assert_called_once_with('cumulative')
#         mock_instance.print_stats.assert_called_once()
#         handle = mock_open()
#         handle.write.assert_called()

# if __name__ == '__main__':
#     unittest.main()
