from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np


def use_numpy_random():
    return np.random.random()


def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random) for _ in range(3)]
        for futures in as_completed(futures):
            print(futures.result())


if __name__ == "__main__":
    main()
