import random
import datetime
import os
import getpass


current_date_time = datetime.datetime.now()
formatted_date_time = current_date_time.strftime("%m-%d-%Y @ %I:%M:%S %p")
working_directory = os.getcwd()
username = getpass.getuser()
print("Current Date and Time:", formatted_date_time)
print("Working Directory:", working_directory)
print("Username:", username)

exit_game = False
user_points = 0
computer_points = 0

while not exit_game:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ")
    
    if user_input == "exit":
        print("Game ended")
        print("You won a total score of " + str(user_points) + " and the computer's total score is " + str(computer_points))
        exit_game = True
    elif user_input in options:
        computer_input = random.choice(options)

        rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

        if user_input == "rock":
            print("Your choice:")
            print(rock)
            if computer_input == "rock":
                print("Computer's choice:")
                print(rock)
                print("It's a tie!")
            elif computer_input == "paper":
                print("Computer's choice:")
                print(paper)
                print("Computer wins!")
                computer_points += 1
            elif computer_input == "scissors":
                print("Computer's choice:")
                print(scissors)
                print("You win!")
                user_points += 1

        elif user_input == "paper":
            print("Your choice:")
            print(paper)
            if computer_input == "rock":
                print("Computer's choice:")
                print(rock)
                print("You win!")
                user_points += 1
            elif computer_input == "paper":
                print("Computer's choice:")
                print(paper)
                print("It's a tie!")
            elif computer_input == "scissors":
                print("Computer's choice:")
                print(scissors)
                print("Computer wins!")
                computer_points += 1

        elif user_input == "scissors":
            print("Your choice:")
            print(scissors)
            if computer_input == "rock":
                print("Computer's choice:")
                print(rock)
                print("Computer wins!")
                computer_points += 1
            elif computer_input == "paper":
                print("Computer's choice:")
                print(paper)
                print("You win!")
                user_points += 1
            elif computer_input == "scissors":
                print("Computer's choice:")
                print(scissors)
                print("It's a tie!")

    else:
        print("Invalid Input")

