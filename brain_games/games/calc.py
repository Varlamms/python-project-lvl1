import random

RULE = 'What is the result of the expression?'

def even():
    use = random.choice(('+', '-', '*'))
    number1 = random.randint(1, 5)
    number2 = random.randint(1, 5)
    question = f'{number1} {use} {number2}'
    if use == '*':
        correct_answer = number1 * number2
    if use == '+':
        correct_answer = number1 + number2
    if use == '-':
        correct_answer = number1 - number2
    return question, str(correct_answer)