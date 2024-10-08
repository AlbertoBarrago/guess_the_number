from utils.utils import set_difficulty, select_random_number, compute_result, show_logo


def start_game():
    show_logo()
    has_guess_number = False
    difficulty = input('Choose a difficulty (easy, medium, hard): ')
    number_of_lives = set_difficulty(difficulty)
    number = select_random_number()
    print(f'I have selected a number between 1 and 100. Can you guess it?')
    # print(f'psst the right number is {number}')
    while not has_guess_number:
        print(f'You have {number_of_lives} lives left.')
        guess = int(input('Enter your guess: '))
        result = compute_result(guess, number)
        if result != 'Congratulations! You guessed it right!' and number_of_lives > 1:
            print(result)
            number_of_lives -= 1
            continue
        elif number_of_lives == 1 and result != 'Congratulations! You guessed it right!':
            print(f'You have run out of lives. Game over. \nThe right number was: {number}')
            has_guess_number = True
        else:
            has_guess_number = True

    has_guess_number = input('Do you want to play again? (y/n)')
    if has_guess_number == 'y':
        start_game()
    else:
        print('Thanks for playing!')


if __name__ == '__main__':
    start_game()
