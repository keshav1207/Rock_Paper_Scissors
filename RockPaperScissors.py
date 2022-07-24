import random
Win = 0
Loss = 0
Draw = 0

while True:
    # Take user input
    user_input = input(" Enter rock,paper or scissors ? \n")
    user_input = user_input.lower().strip()
    if user_input not in ['rock','paper','scissors']:
        print('Enter a valid input')
        continue

    # Make computer choose
    choices = ('rock', 'paper', 'scissors')
    computer_choice = random.choice(choices)
    print(computer_choice)

    # Determine a winner
    if user_input == computer_choice:
            print('Draw!')
            Draw += 1

    elif user_input == "rock":
        if computer_choice == 'paper':
            print('You lose!')
            Loss += 1

        else:
            print('You win!')
            Win += 1

    elif user_input == "scissors":
        if computer_choice == 'paper':
            print('You win!')
            Win += 1

        else:
            print('You lose!')
            Loss += 1

    elif user_input == "paper":
        if computer_choice == 'rock':
            print('You win!')
            Win += 1

        else:
            print('You lose!')
            Loss += 1

    continue_game = input('Do you want to keep playing? Y/N   '  )
    if continue_game != 'y':
        print(f'Your Final score is : Win={Win},Loss={Loss},Draw={Draw}')
        exit()
