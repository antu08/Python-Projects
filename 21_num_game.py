import random

curr_numb = 0
print("Starting 21 Number Game, the person who says 21 loses ")
while True:
    x = input(f'Say number/numbers "Starting from {curr_numb + 1}" [with Space]: ')
    x_list = [int(n) for n in x.split()]
    count = len(x_list)
    
    if (count <= 0 or count > 3):
        print("Error: Entered Invalid numbers")
        continue
    
    print(f"You have entered '{count}' numbers, the numbers are: {x_list} ")
    last_num = x_list[-1]
    player_seq = list(range(curr_numb + 1, curr_numb + 1 + count))
    
    if x_list != player_seq:
        print("Error: Entered wrong Sequence")
        continue
    
    curr_numb = last_num
    if last_num >= 21:
        print('You lost, You Wrote 21 th number \n')
        break
    
    if last_num < 19:
        count = random.randint(1,3)
        computer = list(range(last_num + 1, last_num + 1 + count))
    elif last_num < 21:
        count = random.randint(1,2)
        computer = list(range(last_num + 1, last_num + 1 + count))
    else:
        count = 1
        computer = list(range(last_num + 1, last_num + 1 + count))
    
    print(f'The number provided by computers are: {computer} \n')
    
    last_com_numb = computer[-1]
    curr_numb = last_com_numb
    if last_com_numb >= 21:
        print('Computer lost, Computer wrote 21 th number \n')
        break