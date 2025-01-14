import time

def time_calculation_decorator(func):
    def wrapper(*args):
        start_time = time.process_time_ns()
        func(*args)
        end_time = time.process_time_ns()
        print(f"Time taken to execute the function: {end_time - start_time} ns")
        print(f"stime: {start_time}, etime: {end_time}")
    return wrapper

@time_calculation_decorator
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

measure_me(1000000)