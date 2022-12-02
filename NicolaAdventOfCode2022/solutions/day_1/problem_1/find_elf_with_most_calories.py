import math

from utils.timer import timer_func


@timer_func
def find_elf_with_most_calories(calories):
    max_so_far = -math.inf
    current_sum = 0
    for line in calories:
        if line == "":
            max_so_far = max(max_so_far, current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    max_so_far = max(max_so_far, current_sum)
    return max_so_far


lines = open("../input.txt").read().splitlines()
print(find_elf_with_most_calories(lines))

