import prompt

TOTAL_ROUNDS = 3


def run(game):
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name} !')
    print(game.RULE)
    for _ in range(TOTAL_ROUNDS):
        (question, correct_answer) = game.start_the_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;( "
                  f"Correct answer was ' {correct_answer} '.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
