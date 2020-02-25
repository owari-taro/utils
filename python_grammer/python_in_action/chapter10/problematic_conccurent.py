from concurrent.futures import ThreadPoolExecutor, wait


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        """icrease self.count by 1"""
        self.count += 1


def count_up(counter: Counter):
    for _ in range(10000):
        counter.incremen()


if __name__ == "__main__":
    counter = Counter()
    threads = 2
    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)
    print(counter.count)

