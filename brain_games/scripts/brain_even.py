from random import randint
def main():
    q = randint(0, 555)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if q % 2 == 0:
        correct_answer = "'yes'"
    else:
        correct_answer = "'no'"
    print('Question: ' + str(q))
    answer = input('Your answer: ')
    if answer == 'yes' and q % 2 == 0 or answer == 'no' and q % 2 > 0:
        print('Correct!')
        return True
    else:
        print("'" + answer + "'" + ' is wrong answer ;(.' + ' Correct answer was ' + correct_answer + ".\nLet's try again")
        return False

if __name__ == '__main__':
    main()
