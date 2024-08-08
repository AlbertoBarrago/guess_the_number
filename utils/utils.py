import random


def select_random_number():
    for _ in range(101):
        number = random.randint(1, 100)
        return number


def compute_result(player_number, computer_number):
    if player_number == computer_number:
        return 'Congratulations! You guessed it right!'
    elif player_number > computer_number:
        return 'Your guess is too high. Try again!'
    else:
        return 'Your guess is too low. Try again!'


def set_difficulty(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 5
    else:
        return 1