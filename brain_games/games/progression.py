import random

RULE = 'What number is missing in the progression?'


def start_the_round():
    len_progression = random.randint(5, 10)
    step_progression = random.randint(2, 6)
    current = random.randint(1, 35)
    i = 0
    progression = []
    while i < len_progression:
        progression.append(str(current + step_progression))
        current = current + step_progression
        i = i + 1
    random_index = random.randint(0, (len(progression) - 1))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, str(correct_answer)
