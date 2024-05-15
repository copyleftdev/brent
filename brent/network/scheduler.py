import heapq
import threading
import time

class NetworkTask:
    def __init__(self, priority, task_id, action, *args, **kwargs):
        """
        Initialize a network task with a given priority, task ID, action, and arguments.

        :param priority: Priority of the task (lower number means higher priority).
        :param task_id: Unique identifier for the task.
        :param action: The function to be executed as the task.
        :param args: Positional arguments for the action.
        :param kwargs: Keyword arguments for the action.
        """
        self.priority = priority
        self.task_id = task_id
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def __lt__(self, other):
        return self.priority < other.priority

    def run(self):
        self.action(*self.args, **self.kwargs)

class NetworkTaskScheduler:
    def __init__(self):
        """
        Initialize the NetworkTaskScheduler with an empty priority queue.
        """
        self.task_queue = []
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.worker_thread = threading.Thread(target=self._worker)
        self.worker_thread.start()

    def add_task(self, priority, task_id, action, *args, **kwargs):
        """
        Add a task to the scheduler.

        :param priority: Priority of the task (lower number means higher priority).
        :param task_id: Unique identifier for the task.
        :param action: The function to be executed as the task.
        :param args: Positional arguments for the action.
        :param kwargs: Keyword arguments for the action.
        """
        with self.lock:
            task = NetworkTask(priority, task_id, action, *args, **kwargs)
            heapq.heappush(self.task_queue, task)
    
    def _worker(self):
        while not self.stop_event.is_set():
            with self.lock:
                if self.task_queue:
                    task = heapq.heappop(self.task_queue)
                    task.run()
            time.sleep(0.1)  # Adjust the sleep time as needed

    def stop(self):
        """
        Stop the scheduler and wait for the worker thread to finish.
        """
        self.stop_event.set()
        self.worker_thread.join()

    def get_task_count(self):
        """
        Get the number of tasks in the scheduler.

        :return: The number of tasks in the priority queue.
        """
        with self.lock:
            return len(self.task_queue)
