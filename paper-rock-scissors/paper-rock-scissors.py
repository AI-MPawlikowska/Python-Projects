import random
choice=input("What do you choose? \n Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.: ")

if choice==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

computer_choice=random.randint(0,2)
print(f"Computer chose: {computer_choice}")

if choice==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
