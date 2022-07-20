import time


def result_time(func):
    def time_count():
        start = time.time()
        result = func()
        print(result)
        end = time.time()
        print("total execution timr", end - start)
    return time_count()