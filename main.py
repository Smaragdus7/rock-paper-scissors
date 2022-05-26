import random

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

#Write your code below this line 👇
options = [rock,paper,scissors]
computers_random = random.randint(0,2)
computers_choice = options[computers_random]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[my_choice])
print("Computer chose:")
print(computers_choice)
if my_choice == 0:
  if computers_random == 0:
    print("It's a draw")
  elif computers_random == 1:
    print("You lose")
  else:
    print("You win")
elif my_choice == 1:
  if computers_random == 0:
    print("You win")
  elif computers_random == 1:
    print("It's a draw")
  else:
    print("You lose")
else:
  if computers_random == 0:
    print("You lose")
  elif computers_random == 1:
    print("You win")
  else:
    print("It's a draw")
    