import itertools
import math
import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

def print_permutations(input_string):
    permutations = itertools.permutations(input_string)
    for perm in permutations:
        print(''.join(perm))

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("\nTake a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break