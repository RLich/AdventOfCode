import os

working_dir = os.getcwd()
input_file = working_dir + "\\input.txt"

with open(file=input_file) as raw_input:
    strategy = raw_input.read()


# Part 1
def translate_encryption(symbol):
    if symbol == "A" or symbol == "X":
        symbol = "rock"
    elif symbol == "B" or symbol == "Y":
        symbol = "paper"
    elif symbol == "C" or symbol == "Z":
        symbol = "scissors"
    else:
        print("Symbot cannot be encrypted")
    return symbol


def decide_winner(opponent_shape, my_shape):
    if opponent_shape == my_shape:
        return "draw"
    elif opponent_shape == "rock" and my_shape == "paper":
        return "won"
    elif opponent_shape == "rock" and my_shape == "scissors":
        return "lost"
    elif opponent_shape == "paper" and my_shape == "rock":
        return "lost"
    elif opponent_shape == "paper" and my_shape == "scissors":
        return "won"
    elif opponent_shape == "scissors" and my_shape == "paper":
        return "lost"
    elif opponent_shape == "scissors" and my_shape == "rock":
        return "won"
    else:
        print("Someone used a forbidden shape, cheater!")


def calculate_points(shape, outcome):
    shape_score = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    outcome_score = {
        "lost": 0,
        "draw": 3,
        "won": 6
    }
    return shape_score[shape] + outcome_score[outcome]


match_rounds = strategy.split("\n")  # Split the strategy into rounds
points_list = []

opponent_shape_index = 0
my_shape_index = 2
for match_round in match_rounds:
    opponent_shape = translate_encryption(match_round[opponent_shape_index])
    my_shape = translate_encryption(match_round[my_shape_index])
    print("Opponent shape: %s, my shape: %s" % (opponent_shape, my_shape))
    match_outcome = decide_winner(opponent_shape=opponent_shape, my_shape=my_shape)
    print("Outcome: %s" % match_outcome)
    points_for_round = calculate_points(shape=my_shape, outcome=match_outcome)
    print("Points for the match: %s\n" % points_for_round)
    points_list.append(points_for_round)

print("Total score for part 1: %s" % sum(points_list))
print("\nEnd of Part 1\n//////////////////////////////////////////////////////////////////////////////\nPart 2")
# Part 2


def translate_encryption_updated(symbol):
    if symbol == "Y":
        symbol = "draw"
    elif symbol == "X":
        symbol = "lost"
    elif symbol == "Z":
        symbol = "won"
    else:
        print("Symbot cannot be encrypted")
    return symbol


shape_winning_guide = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}


def choose_shape(opponent_shape, desired_outcome):
    if desired_outcome == "draw":
        chosen_shape = opponent_shape
    elif desired_outcome == "lost":
        winning_shape = shape_winning_guide[opponent_shape]
        chosen_shape = shape_winning_guide[winning_shape]
    elif desired_outcome == "won":
        chosen_shape = shape_winning_guide[opponent_shape]
    else:
        print("Instructions unclear, choosing a gun")
        chosen_shape = "gun"
    return chosen_shape


updated_points_list = []
for match_round in match_rounds:
    opponent_shape = translate_encryption(match_round[opponent_shape_index])
    desired_outcome = translate_encryption_updated(match_round[my_shape_index])
    print("Opponent chooses: %s, desired outcome for me: %s" % (opponent_shape, desired_outcome))
    my_shape = choose_shape(opponent_shape=opponent_shape, desired_outcome=desired_outcome)
    print("Shape I should choose: %s" % my_shape)
    points = calculate_points(shape=my_shape, outcome=desired_outcome)
    print("Points from this round: %s\n" % points)
    updated_points_list.append(points)

print("Total score for part 2: %s" % sum(updated_points_list))
