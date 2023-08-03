# a, x = rock, loss
# b, y = paper, draw
# c, z = scissors

def get_input():
    f = open("in.txt", "r")

    rounds = []
    for line in f.readlines():
        game = line.strip().replace(" ", "")

        round_outcome = []
        for g in game:
            round_outcome.append(g)

        if round_outcome:
            rounds.append(round_outcome)

    f.close()

    return rounds


def calculate_score(game):
    score = 0

    # round[1] == us
    # round[0] ==  opponent
    for round in game:
        round_score = 0

        if round[1] == "Y": # draw
            our_choice = round[0]
            round_score += 3
        elif round[1] == "X": # we have to lose
            if round[0] == "A":
                our_choice = "Z"
            elif round[0] == "B":
                our_choice = "X"
            else:
                our_choice = "Y"
        elif round[1] == "Z": # we have to win
            if round[0] == "A":
                our_choice = "Y"
            elif round[0] == "B":
                our_choice = "Z"
            else:
                our_choice = "X"
            round_score += 6

        # get score from our choice
        if our_choice == "X" or our_choice == "A": round_score += 1
        elif our_choice == "Y" or our_choice == "B": round_score += 2
        elif our_choice == "Z" or our_choice == "C": round_score += 3

        score += round_score

    return score

if __name__=="__main__":
    game = get_input()

    score = calculate_score(game)
    print(score)