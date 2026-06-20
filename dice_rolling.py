import random

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = (dice1, dice2)
    print("Roll The Dice? ")
    x = input("Enter your Choice [Y/N]: ")
    if(x == 'Y' or x == 'y'):
        print(f"Dice output are {result} \n")
    elif(x == 'N' or x == 'n'):
        print(f"Dice are not rolled")
        print('Exiting \n')
        break
    else:
        print(f'Wrong output, you have entered "{x}" instead of Y/N \n')
