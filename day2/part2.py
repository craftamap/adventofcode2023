import sys
import math

file = sys.argv[1]

with open(file) as fh:
    lines = fh.readlines()

def parse_line(line: str):
    [game, rounds] = line.split(":")
    [_,game_id] = game.split(" ")
    rounds: str
    rounds = rounds.strip()
    return {"game_id": int(game_id),  "rounds": parse_rounds(rounds)}

def parse_rounds(rounds: str):
    return [parse_round(x.strip()) for x in rounds.split(";")]

def parse_round(round: str):
    dice = round.split(", ")
    colors_and_numbers = {}
    for die in dice:
        [number, color] = die.strip().split(' ')
        colors_and_numbers[color] = int(number)
    return colors_and_numbers


games = [parse_line(x) for x in lines]

MAX_NUMBERS = {"red": 12, "green": 13, "blue": 14}

def minmax_game(game):
    data = {}
    for round in game["rounds"]:
        for color in MAX_NUMBERS.keys():
            data[color] = max(data.get(color, 0), round.get(color, 0))
    return data

minmaxed = [minmax_game(x) for x in games]
power_of_games = [math.prod(x.values()) for x in minmaxed]
print(sum(power_of_games))
