from utils.timer import timer_func

rps_values = {"X": 1, "Y": 2, "Z": 3}
rps_outcomes = {"X": {"A": 3, "B": 0, "C": 6}, "Y": {"A": 6, "B": 3, "C": 0}, "Z": {"A": 0, "B": 6, "C": 3}}


@timer_func
def get_rps_total_score(rps_rounds):
    total_score = 0
    for rps_round in rps_rounds:
        player_hand = rps_round[2]
        opponent_hand = rps_round[0]
        total_score += rps_values[player_hand] + rps_outcomes[player_hand][opponent_hand]
    return total_score


lines = open("../input.txt").read().splitlines()
print(get_rps_total_score(lines))
