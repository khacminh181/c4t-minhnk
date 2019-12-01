import random

playerX = 3
playerY = 3

enemyX = random.randint(0, 6)
enemyY = random.randint(0, 6)

def printMap(side):
    for i in range(side):
        for j in range(side):
            if i == playerY and j == playerX:
                print(" P ", end="")
            elif i == enemyY and j == enemyX:
                print(" E ", end="")    
            else:
                print(" * ", end="")
        print()

def run():
  global playerX, playerY, enemyX
  # Lay lenh cua ng dung tu console
  direct = input("Your move: ")
  # check lenh va xu ly logic
  if direct.lower() == "up":
    playerY = playerY - 1
  if direct.lower() == "down":
    playerY = playerY + 1
  if direct.lower() == "right":
    playerX += 1
  if direct.lower() == "left":
    playerX -= 1  
    
  enemyX += 1

  if playerX == enemyX and playerY == enemyY: 
    exit(0)

while(True):
  print(chr(27) + "[2J")
  printMap(7)
  run()