#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
last = number % 10
if exe == 1:
    number *= -1
    last *= -1
print(f"Last digit of {number:d} is ", end="")
if last > 5:
    print(f"{last:d} and is greater than 5")
elif last == 0:
    print(f"{last:d} and is 0")
else:
    print(f"{last:d} and is less than 6 and not 0")
