playerX = 3
playerY = 3

def printMap(side):
    for i in range(side):
        for j in range(side):
            if i == playerY and j == playerX:
                print(" P ", end="")
            else:
                print(" * ", end="")

        print()




def run():
  global playerX, playerY
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

printMap(7)

while(True):
  #xu ly logic
  print(chr(27) + "[2J")
  printMap(7)
  run()
  #in lai map