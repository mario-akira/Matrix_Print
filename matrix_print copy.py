import time
import random


def generate_random():
    palavra = random.choice(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúâôãõ,.;:\/_-+= "
    )
    return palavra


def change_letter(original_string, position, new_letter):
    new_word = list(original_string)
    new_word[position] = new_letter
    new_string = ''.join(new_word)
    return new_string


def print_hello_world(target_phrase):
    # target_phrase = "Hello World"
    current_guess = ""
    chosen_letters = []  
    random_letters = {}
    i = 0
    for i in range(0, len(target_phrase)):
        actual_letter_creation = generate_random()
        random_letters[i] = actual_letter_creation
        current_guess += random_letters[i]
    print(current_guess)

    while current_guess != target_phrase:
        for i in range(0, len(current_guess)):
            if current_guess[i] != target_phrase[i]:
                new_letter = generate_random()
                current_guess = change_letter(current_guess, i, new_letter)
                time.sleep(0.004)
        print(current_guess)


print_hello_world("Hello World")