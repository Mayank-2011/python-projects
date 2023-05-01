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


game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[choice])
  import random
  pc_choice = random.randint(0,2)
  print(f"Computer chose:\n{game_images[pc_choice]}")
  
  if choice == 0 and pc_choice == 2:
    print("You Win!")
  elif pc_choice == 0 and choice == 2:
    print ("You lose!")
  elif choice > pc_choice:
    print("You Win!")
  elif pc_choice > choice:
    print("You lose!")
  elif choice == pc_choice:
    print("Its a draw")
