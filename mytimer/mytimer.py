from contextlib import contextmanager

@contextmanager
def elapsed_time():
    import time
    start = time.time()
    yield
    print('Elapsed time:', time.time() - start)