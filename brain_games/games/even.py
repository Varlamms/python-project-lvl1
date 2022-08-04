from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    question = randint(0, 555)
    correct_answer = 'yes'
    if question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
