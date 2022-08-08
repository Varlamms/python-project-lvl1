import random

RULE = 'What number is missing in the progression?'


def generate_round_data():
    progression_length = random.randint(5, 10)
    step_progression = random.randint(2, 4)
    current = random.randint(1, 25)
    i = 0
    progression = []
    while i < progression_length:
        progression.append(str(current + step_progression))
        current = current + step_progression
        i = i + 1
    random_index = random.randint(0, progression_length)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, str(correct_answer)
