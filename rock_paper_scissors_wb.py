import random

print('Hi! This is command line Rock, Paper, Scissors game')

possible_choices = ['Rock','Paper','Scissors']
no_player_wins = 0
no_bot_wins = 0

def rock_paper_scissors():
    global no_player_wins
    global no_bot_wins
    player_choose = input('Player, choose Rock/Paper/Scissors: ')
    computer_choose = random.choice(possible_choices)
    print('Computer choose:', computer_choose)
    if player_choose=='Rock' and computer_choose == 'Paper':
        print('Bot wins')
        no_bot_wins +=1
    elif player_choose=='Rock' and computer_choose == 'Scissors':
        print('Player  wins')
        no_player_wins +=1
    elif player_choose=='Paper' and computer_choose == 'Scissors':
        print('Bot wins')
        no_bot_wins +=1
    elif player_choose=='Paper' and computer_choose == 'Rock':
        print('Player  wins')
        no_player_wins +=1
    elif player_choose=='Scissors' and computer_choose == 'Rock':
        print('Bot wins')
        no_bot_wins +=1
    elif player_choose=='Scissors' and computer_choose == 'Paper':
        print('Player  wins')
        no_player_wins +=1
    elif player_choose==computer_choose:
        print('This is tie')
    else:
        print("Player, you can choose only Rock or Paper or Scissors")
    print("Player no of wins: ", no_player_wins)
    print("Bot no of wins: ", no_bot_wins)

next_game = True
while next_game:
    rock_paper_scissors()
    next_time_input = input('Do you want to play next time? y/n')
    if next_time_input == 'n':
        next_game = False


