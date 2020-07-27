# no. of guesses 9
# print no. of guesses left
# no. of guesses he took to finish
# game over
n = 18
i = 1
print(" Max number of guesses = 9 ")
while (i <= 9):
    num = int(input("Guess the number:\n"))
    if num > 18:
        print("Try a number smaller than this")
    elif num < 18:
        print("Try a number greater than this")
    else:
        print("You WON!!!")
        print("No. of attempts: "+str(i))
        break
    print("Attempts left: " + str(9 - i))
    i += 1
if i > 9:
    print("Game Over")