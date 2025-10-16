import random


def roll():
    min_value = 1
    max_value = 6
    roll=random.randint(min_value, max_value)
    
    return roll


while True:
    players=input("enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("must between 2-4 players only")
    else:
        print("invalid,try again")
        
max_score=50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for players_ind in range(players):
        print("\nPlayer number", players_ind +1, "turn has just started!")
        print("\n your total score is:",players_score[players_ind],"\n")
        current_score = 0
                
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() !="y":
                break
            
            value = roll()
            if value ==1:
                print("you rolled a 1! turn done!")
                current_score = 0
                
            else:
                current_score += value
                print("you rolled a",value)
            
            print("your score is:",current_score)
            
        players_score[players_ind] += current_score
        print("your total score is :",players_score[players_ind])

max_score = max(players_score)
winning_ind = players_score.index(max_score)
print("Player number",winning_ind +1 , "is the winner with score of:", max_score)                
                
                
            