import time
from contextlib import contextmanager


@contextmanager
def timer(message: str):
    start = time.perf_counter()
    yield
    time_in_ms = (time.perf_counter() - start) * 1000
    print(f"Elapsed time (ms) {message}: {time_in_ms}")
