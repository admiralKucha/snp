class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(list):
    if len(list) != 2:
        raise WrongNumberOfPlayersError("WrongNumberOfPlayersError")
    if not {list[0][1], list[1][1]}.issubset({'R', 'P', 'S'}):
        raise NoSuchStrategyError("NoSuchStrategyError")

    if list[0][1] == "R":
        if list[1][1] == "P":
            return list[1][0] + ' P'
        else:
            return list[0][0] + ' R'

    if list[0][1] == "S":
        if list[1][1] == "R":
            return list[1][0] +' R'
        else:
            return list[0][0] + ' S'

    if list[0][1] == "P":
        if list[1][1] == "S":
            return list[1][0] +' S'
        else:
            return list[0][0] +' P'

try:
    print( rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) )
except Exception as e:
    print(e)

try:
    print( rps_game_winner([['player1', 'P'], ['player2', 'A']]) )
except Exception as e:
    print(e)

try:
    print( rps_game_winner([['player1', 'A'], ['player2', 'P']]) )
except Exception as e:
    print(e)

try:
    print( rps_game_winner([['player1', 'A'], ['player2', 'A']]) )
except Exception as e:
    print(e)

print()
print( rps_game_winner([['player1', 'P'], ['player2', 'S']]) )
print( rps_game_winner([['player1', 'P'], ['player2', 'P']]) )
print( rps_game_winner([['player1', 'P'], ['player2', 'R']]) )
print()
print( rps_game_winner([['player1', 'S'], ['player2', 'S']]) )
print( rps_game_winner([['player1', 'S'], ['player2', 'P']]) )
print( rps_game_winner([['player1', 'S'], ['player2', 'R']]) )
print()
print( rps_game_winner([['player1', 'R'], ['player2', 'S']]) )
print( rps_game_winner([['player1', 'R'], ['player2', 'P']]) )
print( rps_game_winner([['player1', 'R'], ['player2', 'R']]) )
