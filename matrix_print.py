import time
import random


def print_hello_world(target_phrase):
    # target_phrase = "Hello World"
    current_guess = ""
    chosen_letters = []

    while current_guess != target_phrase:
        i = 0
        while i < len(target_phrase):
            random_letter = random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúâôãõà,.;:\/_-+= ")
            if random_letter not in chosen_letters:
                if random_letter != target_phrase[i]:
                    print(current_guess + random_letter)
                    time.sleep(0.01)
                    chosen_letters.append(random_letter)
                else:
                    current_guess += random_letter
                    print(current_guess)
                    i += 1
                    chosen_letters = []


print_hello_world("Hello World")