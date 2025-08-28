import random

while True:
    list = ['rock', 'paper', 'scissor']
    computer = random.choice(list)
    x = input('Enter your choice (rock/paper/scissor [No to Exit] ): ')
    if(x == 'rock' and computer == 'paper'):
        print('Computer won')
        print(f'computer selected {computer}')
            
    elif(x == 'rock' and computer == 'scissor'):
        print('You won')
        print(f'computer selected {computer}')
            
    elif(x == 'paper' and computer == 'rock'):
        print('You won')
        print(f'computer selected {computer}')
            
    elif(x == 'paper' and computer == 'scissor'):
        print('Computer won')
        print(f'computer selected {computer}')
            
    elif(x == 'scissor' and computer == 'rock'):
        print('Computer won')
        print(f'computer selected {computer}')
            
    elif(x == 'scissor' and computer == 'paper'):
        print('You won')
        print(f'computer selected {computer}')
        
    elif(x.lower() == 'no'):
        print('Exiting..')
        break
     
    else:
        print('Both have same value')
        print(f'computer selected {computer}')
