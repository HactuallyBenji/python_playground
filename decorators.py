def log_call_count(func_to_wrap):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        return func_to_wrap(*args, **kwargs)

    return wrapper

@log_call_count
def add_with_log(a, b):
    return a + b

@log_call_count
def subtract_with_log(a, b):
    return a - b

add_with_log(2, 3)
# Prints: Called 1 times
add_with_log(4, 5)
# Prints: Called 2 times
subtract_with_log(7, 2)
# Prints: Called 1 times
