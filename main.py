from func import *
from tkinter import *
import os
window = Tk()
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
playing = True
done = False
turn = 0
while playing:
    print("turn number " + str(turn) + " player " + str(turn % 2) + " please make a move")
    draw(spots)
    selection = input("where would u like to place you mark? ")

    if str.isdigit(selection) and int(selection) in spots:
        if not spots[int(selection)] in ["0", "X"]:
            turn = turn + 1
            spots[int(selection)] = check(turn)
            winning(spots)
        else:
            print("sorry this spot is taken")
    if winning(spots): playing, done = False, True
    if turn > 8: playing = False
draw(spots)
if turn % 2 == 0:
    print("player 0 won")
else:
    print("player X won")
window.mainloop()