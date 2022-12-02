from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        elapsed_time = t2-t1
        print(f'Function {func.__name__!r} executed in {elapsed_time:.4f} seconds')
        print(f'{(elapsed_time*1000):.4f} milliseconds')
        print(f'{(elapsed_time*1000000):.4f} microseconds')
        return result
    return wrap_func
