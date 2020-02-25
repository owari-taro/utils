import threading
from concurrent.futures import ThreadPoolExecutor, wait
from python_grammer.python_in_action.chapter10.problematic_conccurent import count_up


class ThreadSafeCounter:
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def incremtn(self) -> None:
        """increase count by 1 with thread safe"""
        with self.lock:
            self.count += 1


if __name__ == "__main__":
    counter = ThreadSafeCounter()
    threads = 2
    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)

    print(counter.count)
