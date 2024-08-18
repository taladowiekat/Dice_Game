import random

def roll():
    # the range of number on the dice roll
    min_val = 1
    max_val =6
    # roll the dice
    roll_dice = random.randint(min_val, max_val)
    return roll_dice

# start loop to get the number of players between 2 and 4
while True :
    players = input('please enter the number of players (2 - 4) :')
    # check if the input is a valid number
    if players.isdigit():
        players = int(players) # convert the input to an integer
        if players in range(2 , 5): # check if the number of players is between 2 and 4
            break
        else : 
            print ('the number of players must be between 2 and 4')
    else : 
        print("invalid number of players")

max_score = 50
player_score = [0 for _ in range(players)]
# print (player_score)

while max(player_score) < max_score:
    for idx in range(players):
        print('player' , idx+1 ,'starting playing \n')
        print('your score is' , player_score[idx] , '\n')
        current_score = 0
    
    while True:
        wont_play = input('do you want to play? (y/n):')
        if wont_play.lower() != 'y' or wont_play.lower() == 'n':
            break

        value = roll()
        if value == 1:
            print('you get 1 😓 your score is 0')
            current_score = 0
            break
        else:
            print(" you get a :" , value)
            current_score += value
            print('your score is :' , current_score)

    player_score [idx] += current_score
    print("your total score is :" , player_score[idx])
    current_score = 0


max_score = max(player_score)
winner = player_score.index(max_score)
print("winner is :" , winner+1 , 'he`s score is :' ,max_score)
