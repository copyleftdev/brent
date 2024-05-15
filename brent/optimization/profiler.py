import cProfile
import pstats
import io

class Profiler:
    def __init__(self):
        """
        Initialize the Profiler class.
        """
        self.profiler = cProfile.Profile()

    def start(self):
        """
        Start the profiler.
        """
        self.profiler.enable()

    def stop(self):
        """
        Stop the profiler.
        """
        self.profiler.disable()

    def print_stats(self, sort_by='cumulative'):
        """
        Print the profiling statistics.

        :param sort_by: The criterion by which to sort the profiling results (default: 'cumulative').
        """
        stream = io.StringIO()
        stats = pstats.Stats(self.profiler, stream=stream).sort_stats(sort_by)
        stats.print_stats()
        print(stream.getvalue())

    def save_stats(self, filename, sort_by='cumulative'):
        """
        Save the profiling statistics to a file.

        :param filename: The name of the file to save the profiling results to.
        :param sort_by: The criterion by which to sort the profiling results (default: 'cumulative').
        """
        with open(filename, 'w') as file:
            stats = pstats.Stats(self.profiler, stream=file).sort_stats(sort_by)
            stats.print_stats()
