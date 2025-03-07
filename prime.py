import time
import math

def current_milli_time():
    return round(time.time() * 1000)

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True  # 2 is the only even prime
    if x % 2 == 0:
        return False  # Exclude other even numbers

    # Check up to sqrt(x), skipping even numbers
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

rs = 1000
re = 40000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re - rs), "numbers searched in", end - start, "milliseconds")
