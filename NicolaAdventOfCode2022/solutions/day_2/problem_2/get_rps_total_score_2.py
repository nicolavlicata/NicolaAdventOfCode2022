from day_2.common import rps_values, rps_outcomes, rps_should_play
from utils.timer import timer_func


@timer_func
def get_rps_total_score_2(rps_rounds):
    total_score = 0
    for rps_round in rps_rounds:
        player_outcome = rps_round[2]
        opponent_hand = rps_round[0]
        player_hand = rps_should_play[player_outcome][opponent_hand]
        total_score += rps_values[player_hand] + rps_outcomes[player_hand][opponent_hand]
    return total_score


lines = open("../input.txt").read().splitlines()
print(get_rps_total_score_2(lines))
