#!/usr/bin/env python3
import scripts_brain_even
import cli

def main():
    print("Welcome to the Brain Games")

if __name__ == '__main__':
    main()



def welcome_user():
    name = input('May I have your name? ')
    print("Hello, " + name + "!")

if __name__ == '__main__':
    cli.welcome_user()
    

scripts_brain_even.main()

input ('stop')