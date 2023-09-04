import random
def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors)')
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options) 
    choices = {'player':player_choice, 'computer': computer_choice}
    return choices

def get_winner(player,computer):
    print(f'You chose {player}, and the computer chose {computer}')
    if player == computer:
        return 'tie'
    elif player == 'rock':
       if computer == 'paper':
         return 'computer wins'
       else:
         return 'you win'
    elif player == 'paper':
       if computer == 'scissors':
         return 'computer wins'
       else:
         return 'you win'
    elif player == 'scissors':
       if computer == 'rock':
         return 'computer wins'
       else:
         return 'you win'

choices = get_choices()
result = get_winner(choices['player'],choices['computer'])
print(result)
