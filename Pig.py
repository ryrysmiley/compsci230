import random
game = True

playerscore = 0
computerscore = 0
roll = 0
turn_score = 0

#functions
def rolldice():
    return random.randint(1,6)

def printscores():
    print("Your Score:", playerscore)
    print("Computer Score:", computerscore)

def checkscore():
    playing = True
    if playerscore >= 100 or computerscore >= 100:
        playing = False
    if playerscore >= 100:
        print("You win!")
    if computerscore >= 100:
        print("Computer wins!")
    return playing

def p_roll():
    p_turn = 0
    choice = input("r or h?(default is h)")
    while choice.lower() == "r":
        roll = rolldice()
        print("Roll:", roll)
        if roll == 1:
            p_turn = 0
            print("Zero points on player's turn.")
            break
        else:
            p_turn += roll
            print("Sum of rolls:", p_turn)
            choice = input("r or h?(default is h)")
    print("Player turn is over.")
    return p_turn

def c_roll():
    c_turn = 0
    while c_turn < 20:
        roll = rolldice()
        print("Roll:", roll)
        if roll == 1:
            c_turn = 0
            print("Zero points on computer's turn.")
            break
        else:
            c_turn += roll
            print("Sum of rolls:", c_turn)
    print("Computer's turn is over.")
    return c_turn

print("Welcome to game.")

#gameplay
while game:
    playerscore += p_roll()
    game = checkscore()
    printscores()
    if game:
        computerscore += c_roll()
        game = checkscore()
        printscores()
