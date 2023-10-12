import cProfile
import time

def function1():
    print("Function 1 starts...")
    time.sleep(1)
    sum_ = 0
    for i in range(100000):
        sum_ += i
    print("Function 1 ends...")

def function2():
    print("Function 2 starts...")
    time.sleep(2)
    sum_ = 1
    for i in range(1, 100000):
        sum_ *= i
    print("Function 2 ends...")

def function3():
    print("Function 3 starts...")
    time.sleep(3)
    print("Function 3 ends...")

def profile_function(func):
    profiler = cProfile.Profile()
    profiler.enable()
    
    func()
    
    profiler.disable()
    profiler.print_stats(sort='time')

if __name__ == '__main__':
    profile_function(function1)
    profile_function(function2)
    profile_function(function3)
