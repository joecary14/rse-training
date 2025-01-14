<<<<<<< HEAD
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
@my_decorator
def say_goodbye():
    print("Goodbye!")
    
say_goodbye()
say_hello()
=======
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
>>>>>>> 8b004ef (Practice exercises)
