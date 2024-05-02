# practice using nested list and random number
# make a nested list, where my number is list1, list2, list3; the computer generated numbers is the index of the lists
# so, the result would be the value seleted in the nested list
#             rock(0)   paper(1)   scissor(2) (computer)
# rock(0)      draw      lose        win
# paper(1)      win      draw        lose
# scissor(2)    lose      win        draw


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

import random

def rock_paper_scissors():
  compNumber = random.randint(0,2)
  yourInput = int(input("Enter a number among 0, 1 and 2.\n0 -> rock, 1 -> paper, 2 -> scissor: "))
  if int(yourInput)== 0 or int(yourInput)== 1 or int(yourInput)==2:
    if compNumber == 0:
     print("The computer has: " + rock)
    elif compNumber == 1:
     print("The computer has: " + paper)
    elif compNumber == 2:
     print("The computer has: " + scissors)
    
    if yourInput == 0:
     print("You have: " + rock)
    elif yourInput == 1:
     print("You have: " + paper)
    elif yourInput == 2:
     print("You have: " + scissors)
 
   
    resultMap = [["A draw!", "You lose!", "You win!"], ["You win!", "A draw!", "You lose!"], ["You lose!", "You win!", "A draw!"]]
    print("\nResult: " + resultMap[yourInput][compNumber])
  else:
    print("Wrong number! Please restart the game and enter a valid number from 0 to 2!")


def main():
  rock_paper_scissors()
 

if __name__ == "__main__":
    main()