import random 
import sys
from random import randint
Run = True

#Checks score to see who the winenr is
def Score_check(Player_move, Bot_move):
  if(Player_move == Bot_move):
    print("Draw")
  elif(Player_move == 1 and Bot_move == 3):
    print("Player wins")
  elif(Player_move == 1 and Bot_move == 2):
    print("Bot wins")
  elif(Player_move == 3 and Bot_move == 1):
    print("Bot wins")
  elif(Player_move == 1 and Bot_move == 3):
    print("Player wins")


while Run == True:

  #Checks to see if the player wants to play
  Game_play_check = int(input("\nDo you want to play Another rounds? \n1)Yes\n2)No\n")
  )
  if Game_play_check == 2:
    Run == False
    sys.exit()
  
  #Collects game data
  Player_move = int(input("Pick your move\n\n1)Rock \n2)Papper\n3)Scissors\n\n"))
  Bot_move = random.randrange(0,4)

  print("Bot Move is", Bot_move, " Player_move", Player_move)

#Runs functiins to check who wins
  Score_check(Player_move,Bot_move)
