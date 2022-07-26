#!/usr/bin/env python3
from random import randint
import cli

def main():
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    q = randint (0, 555)
    if q % 2 == 0:
        correct_answer = "'yes'"
    else:
        correct_answer = "'no'"
    for _ in range(3):
        q = randint(0, 555)
        print('Question: '+ str(q))
        answer = input('Your answer: ')
        if answer == 'yes' and q % 2 == 0 or answer == 'no' and q % 2 > 0:
            print('Correct')
        else:
            print("'" + answer + "'" + ' is wrong answer ;(.' + ' Correct answer was ' + correct_answer + ".\nLet's try again, ")
            break
if __name__ == '__main__':
    main()

