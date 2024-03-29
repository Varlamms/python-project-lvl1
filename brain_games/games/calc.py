import random

RULE = 'What is the result of the expression?'


def generate_round_data():
    action = random.choice(('+', '-', '*'))
    number1 = random.randint(1, 5)
    number2 = random.randint(1, 5)
    question = f'{number1} {action} {number2}'
    if action == '*':
        correct_answer = number1 * number2
    if action == '+':
        correct_answer = number1 + number2
    if action == '-':
        correct_answer = number1 - number2
    return question, str(correct_answer)
