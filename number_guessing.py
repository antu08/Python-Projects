import random

numb = random.randint(1,100)
print('Computer has selected a number')
count = 0
while True:
    x = int(input('Enter Your Guess (between 1 to 100): '))
    if(numb == x):
        count = count + 1
        print(f'You have Guessed the number "{numb}" correctly in "{count}" attempts \n')
        print('Thanks for playing, Bye \n')
        break
    elif(numb > x):
        count = count + 1
        print(f'Your Guess number {x} is lesser, select a greater number')
    elif(numb < x):
        count = count + 1
        print(f'Your Guess number {x} is greater, select a lesser number')
