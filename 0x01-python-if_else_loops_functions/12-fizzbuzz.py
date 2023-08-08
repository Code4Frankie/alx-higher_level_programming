#!/usr/bin/python3

def fizzbuzz():
    for nm in range(1, 101):
        if nm % 3 == 0 and nm % 5 != 0:
            print('Fizz', end=' ')
        elif nm % 5 == 0 and nm % 3 != 0:
            print('Buzz', end=' ')
        elif nm % 3 == 0 and nm % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(nm, end=' ')

