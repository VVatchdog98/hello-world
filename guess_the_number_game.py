from random import randint
from math import log

print('=== Welcome to the guessing game: type "quit" to exit:') #Welcome to the program

low_num_x = int(input('Enter low number: ')) #asking for user input for a range between 2 numbers
high_num_y = int(input('Enter high number: '))
number_of_chances = round(log(high_num_y - low_num_x + 1, 2)) #using log from math, to get logarithmic number
random_number = randint(low_num_x, high_num_y) #generating random number between X and Y

print(f'You have {number_of_chances} chances to win')
print('--|The game begins|--')
print(f'\n|Guess the random number in between {low_num_x} and {high_num_y}|')

command = input(f'Enter a Guessing number: ')

while command != 'quit': # while loop for X amount of chances

    guess = int(command)

    if guess == random_number:
        print('Congratz!! --- You WON! ---')
        print(f'in {number_of_chances} try.')
        print('Start a new game:')
        break

    number_of_chances -= 1
    if number_of_chances == 0:
        print(f'\nYou ran out of chances.\nStart a new game:')
        break

    if guess > random_number:
        print('Try again. You guessed too high!')
        print(f'{number_of_chances} try left.')
    elif guess < random_number:
        print('Try again. You guessed too low!')                         #simple_terminal_game_using_mostly_logic_with_basic_code_skill
        print(f'{number_of_chances} try left.')                                                                          #first_project :Deniel Mihaylov

    command = input(f'Enter a Guessing number: ')

