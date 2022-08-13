"""
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors

"""
def rpsls(pl1, pl2):
    d={
        "scissors":("paper","lizard")
        ,"paper":("rock","spock")
        ,"rock":("lizard","scissors")
        ,"lizard":("spock","paper")
        ,"spock":("rock","scissors")
        }

    if(pl1==pl2):return "Draw!"
    elif(pl2 in d[pl1]): return "Player 1 Won!"
    else:
        return "Player 2 Won!"




assert(rpsls('rock', 'lizard')== 'Player 1 Won!')
assert(rpsls('paper', 'rock')== 'Player 1 Won!')
assert(rpsls('scissors', 'lizard')== 'Player 1 Won!')
assert(rpsls('lizard', 'paper')== 'Player 1 Won!')
assert(rpsls('spock', 'rock')== 'Player 1 Won!')
assert(rpsls('lizard','scissors')== 'Player 2 Won!')
assert(rpsls('spock','lizard')== 'Player 2 Won!')
assert(rpsls('paper','lizard')== 'Player 2 Won!')
assert(rpsls('scissors','spock')== 'Player 2 Won!')
assert(rpsls('rock','spock')== 'Player 2 Won!')
assert(rpsls('rock', 'rock')== 'Draw!')
assert(rpsls('spock', 'spock')== 'Draw!')
print("done")