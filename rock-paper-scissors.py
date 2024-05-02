# practice using nested list and random number
# make a nested list, where my number is list1, list2, list3; the computer generated numbers is the index of the lists
# so, the result would be the value seleted in the nested list
#             rock(0)   paper(1)   scissor(2) (computer)
# rock(0)      draw      lose        win
# paper(1)      win      draw        lose
# scissor(2)    lose      win        draw

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
myList = [rock, paper, scissors]

def rock_paper_scissors():
  compChoice = random.randint(0,2)
  userInput = int(input("Enter a number among 0, 1 and 2.\n0 -> rock, 1 -> paper, 2 -> scissor: "))
  if userInput== 0 or userInput== 1 or userInput==2:
    print("The computer has: " + myList[compChoice])
    print("You have: " + myList[userInput])
    resultMap = [["A draw!", "You lose!", "You win!"], ["You win!", "A draw!", "You lose!"], ["You lose!", "You win!", "A draw!"]]
    print("\nResult: " + resultMap[userInput][compChoice])
  else:
    print("Wrong number! Please restart the game and enter a valid number: 0, 1, or 2!")


def main():
  rock_paper_scissors()
 

if __name__ == "__main__":
    main()