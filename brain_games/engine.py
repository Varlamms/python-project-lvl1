import prompt

TOTAL_ROUNDS = 3



def run(game):
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,' + name + '!')
    print(game.RULE)
    for _ in range(TOTAL_ROUNDS):
        (question, correct_answer) = game.even()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            print("Correct!")
        else:
            print("'" + answer + "'" + ' is wrong answer ;(.' + ' Correct answer was ' + correct_answer + ".\nLet's try again, " + name)
            break
    else:
        print('Congraturations, ' + name + '!')

    