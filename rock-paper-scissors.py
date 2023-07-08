import random

ruleSet = ["rock","paper","scissors"]

while True:
  
  pc = random.choice(ruleSet)
  human = input("choice: ").lower()
  if human not in ruleSet:
    print("Please choose between rock, paper and scissors")
    continue
  else:
    if pc == human:
      print(f"PC - {pc} | Human - {human}")
      print("draw. . . .Try again")
    elif pc == "rock" and human == "scissors" or pc == "scissors" and human == "paper" or pc ==   "paper" and human == "rock":
      print(f"PC - {pc} | Human - {human}")
      print("You loose . . .Please try again")

    else:
      print(f"PC - {pc} | Human - {human}")
      print("You won!")
      break
