# To Do: Write decorator call_counter that takes path to file as argument.
# Decorated function should log total number of calls to passed file.
# Several functions could log to the same file.

import os
def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if os.path.exists(path):
                with open(path, 'r') as file:
                    lines = file.readlines()
                    call_count = 0
                    for line in lines:
                        if f"Function '{func.__name__}' was called" in line:
                            call_count += 1
            else:
                call_count = 0
            call_count += 1
            with open(path, 'a') as file:
                file.write(f"Function '{func.__name__}' was called {call_count} times\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(3, 5))