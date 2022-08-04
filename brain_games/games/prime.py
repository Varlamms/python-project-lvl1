import random
from math import sqrt

RULE = 'yes" if given number is prime. Otherwise answer "no".'


def even():
    number = random.randint(1, 50)
    correct_answer = 'no'
    if is_prime(number):
        correct_answer = 'yes'
    return number, correct_answer


def is_prime(num):
    if num <= 1:
        return False
    divisor = 2
    while divisor <= sqrt(num):
        if num % divisor == 0:
            return False
        divisor += 1
    return True
