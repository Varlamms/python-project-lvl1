import random

RULE = "Find the greatest common divisor of given numbers."

def even():
    first_chance = random.randint(1, 100)
    second_chance = random.randint(1, 100)
    question = (f'{first_chance} {second_chance}')
    return question, str(are_looking_for(first_chance, second_chance))

def are_looking_for(num1, num2):
    max_divisor = num1
    if num1 % num2 == 0:
        max_divisor = num2
    else:
        big_num = max(num2, num1)
        small_num = min(num2, num1)
        result = big_num % small_num
        while result != 0:
            result = big_num % small_num
            if big_num / small_num == int(big_num / small_num):
                max_divisor = small_num
                break
            big_num = small_num
            small_num = result
    return max_divisor