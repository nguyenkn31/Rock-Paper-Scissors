import random

def game():
    num_games = int(input('Welcome! How many times would you like to play?\n'))
    i = 0
    while i < num_games:
        i += 1
        print('*******************************')
        print(choice_return())

def choice_return():
    numbwin = 0
    user_input = input('Enter your choices: \n"r" for rock \n"p" for paper\n"s" for scissors\n')
    user_input.lower()
    computer_choice = random.choice(['r', 'p', 's'])

    if user_input == computer_choice:
        return "You and the computer both chose {}. It is a tie this time!".format(computer_choice)

    if determine_win(user_input, computer_choice):
        return "You chose {} and the computer chose {}. You won!".format(user_input, computer_choice)

    return "You chose {} and the computer chose {}. You lost!".format(user_input, computer_choice)

def determine_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False

if __name__ == '__main__':
    game()