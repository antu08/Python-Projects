import random

print("Computer Guessed A '4' Digit Unique Number (with no repeatation of Digit and no '0') ")
x = random.sample("123456789", 4)
code = [int(n) for n in x]
attempt = 0

while True:
    y = int(input("Enter your Guess (4 digit number with no repeated Digit): "))
    guess = [int(m) for m in str(y)]
    length = len(guess)
    if(length != 4):
        print("Error: Entered Invalid Number ")
        continue
    
    if len(set(guess)) != 4:  #For checking repeated digit with set(), as set() drop duplicates
        print("Error: Entered Repeated Number ")
        continue
    
    count = 0
    for i in range(length):
        if(guess[i] == code[i]):
            count = count + 1

    attempt = attempt + 1
    if(count == 4):
        print(f'Correct, You have Guessed the secret code correctly {code} in "{attempt}" Attempts \n')
        break
    
    cows, bulls = 0,0
    
    for i in range(length):
        if(code[i] == guess[i]):
            bulls = bulls + 1
        else:
            for j in range(length):
                if ( i == j):
                    continue 
                elif(guess[j] == code[i]):
                    cows = cows + 1
    
    print(f'Your Guess have "{bulls}" bulls and "{cows}" cows \n')
