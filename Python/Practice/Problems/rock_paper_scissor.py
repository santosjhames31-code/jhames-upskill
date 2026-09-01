import random
lives = 3
ai_lives = 3

while lives != 0 and ai_lives != 0:

    rps = ('rock','paper', 'scissor') 
    ai = random.choice(rps)

    while True:
        player = input("Rock, Paper or Scissor? : ")
        player = player.lower()
        if player in rps:
            break
        else:
            print('Invalid choice, please enter rock, paper or scissor.')

    
    if player == ai:
        status = "Draw"
    elif player == 'rock' and ai == 'scissor':
        status = "Player wins"
        ai_lives -= 1
    elif player == 'scissor' and ai == 'paper':
        status = "Player wins"
        ai_lives -= 1
    elif player == 'paper' and ai == 'rock':
        status = "Player wins"
        ai_lives -= 1
    else:
        status = "Player lost"
        lives -= 1

    print(f'Player  : {player}')
    print(f'AI      : {ai}')
    print(f"Status  : {status}")
    print(f"Player  : {lives * '❤ '} | AI : {ai_lives * '❤ '}")
    print()

if lives == 0:
    print("AI wins the game")
else: 
    print("Player wins")
