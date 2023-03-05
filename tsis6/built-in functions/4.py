import time

value = int(input())
delay = int(input())
time.sleep(delay / 1000)
print(f"Square root of {value} after {delay} miliseconds is", pow(value, 0.5))