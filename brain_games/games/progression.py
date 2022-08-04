import random

RULE = 'What number is missing in the progression?'


def even():
    len_progression = random.randint(5, 10)
    step_progression = random.randint(2, 6)
    current = random.randint(1, 35)
    i = 0
    progression = []
    while i < len_progression:
        progression.append(str(current + step_progression))
        current = current + step_progression
        i = i + 1
    hidden = random.randint(0, (len(progression) - 1))
    correct_answer = progression[hidden]
    progression[hidden] = '..'
    question = ' '.join(progression)
    return question, str(correct_answer)
