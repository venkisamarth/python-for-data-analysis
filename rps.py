import sys
import random
# value =input("please enter a vlaue\n")
# print(value)
playrchoice =input("Enter...\n1 for Rock,\n2 for paper,or \n3 for Scissor:\n\n")
player=int(playrchoice)
if playrchoice <1| player>3: 
    sys.exit("you must enter 1,2,or 3.")
computerchoice=random.choice("123")
computer =int(computerchoice)

print("")
print("You choice "+playrchoice+".")
print("python chose"+computerchoice+".")


