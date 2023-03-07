#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print('Last digit of ', number, 'is', end=' ')
number = abs(number) % 10

