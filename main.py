#Dice rolling Game

import random

dice_number = {
  1:'\u2680',
  2:'\u2681',
  3:'\u2682',
  4:'\u2683',
  5:'\u2684',
  6:'\u2685'
}
Balance = 0.00

def dice_rolling(Balance):
  die_one = random.choice(range(1,7))
  die_two = random.choice(range(1,7))
  print(f"{dice_number.get(die_one)} | {dice_number.get(die_two)}")
  print()
  Amount_per_roll = 1
  Balance -= Amount_per_roll
  print(f"Balance :R {Balance:.2f}")
  return Balance

def deposit(Balance):
  print("***************************")
  while True:
    amount = float(input("Enter Deposit Amount :"))
    if amount <= 0:
      print("Invalid Amount.")
      continue
    else:
      Balance += amount
      print(f"Deposited Amount: R{Balance:.2f}")
      print("***************************")
      return Balance


print("***************************")
print("*** WELCOME TO DICE ROLL **")
Balance = deposit(Balance)


running = True

while running:

  user_input = input("Do you want to Roll the Dice? (y/n) :").lower()
  if user_input == "y":
    print("Loading...")
    if Balance <= 0:
      print("You have Insufficient Money.")
      continue
    else:
      Balance = dice_rolling(Balance)
  elif user_input == "n":
    print("---THANK YOU FOR PLAYING---")
    break
  else:
    print(f"{user_input} is Invalid...Try again")
    break