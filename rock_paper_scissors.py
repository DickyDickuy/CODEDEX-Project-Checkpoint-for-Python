from random import randint as kocok

user_choice = int(input("1) ✊\n2) ✋\n3) ✌\npick a number: "))
if user_choice == 1:
    user_choice_name = 'Rock'
    print("You chose ✊")
elif user_choice == 2:
    user_choice_name = 'Paper'
    print("You chose ✋")
elif user_choice == 3:
    user_choice_name = 'Scissors'
    print("You chose ✌")
else:
    print("Invalid choice! Please choose a number between 1 and 3.")
    exit()

computer = kocok(1, 3)
if computer == 1:
    computer_choice_name = 'Rock'
    print("CPU chose ✊")
elif computer == 2:
    computer_choice_name = 'Paper'
    print("CPU chose ✋")
elif computer == 3:
    computer_choice_name = 'Scissors'
    print("CPU chose ✌")

if user_choice == computer:
    print("It's a tie!")
elif (user_choice == 1 and computer == 3) or (user_choice == 2 and computer == 1) or (user_choice == 3 and computer == 2):
    print("You win!")
else:
    print("CPU wins!")
