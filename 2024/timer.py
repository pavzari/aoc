import time
from contextlib import contextmanager


@contextmanager
def timer(message: str):
    start = time.perf_counter()
    yield
    elapsed_time = time.perf_counter() - start
    time_in_ms = elapsed_time * 1000
    print(f"Elapsed time {message}: {time_in_ms:.3f} ms ({elapsed_time:.6f} seconds)")
