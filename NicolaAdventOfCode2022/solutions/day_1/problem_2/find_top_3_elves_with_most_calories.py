import heapq

from utils.timer import timer_func


@timer_func
def find_top_3_elves_with_most_calories(calories):
    max_heap = []
    current_sum = 0
    for line in calories:
        if line == "":
            heapq.heappush(max_heap, -1 * current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    heapq.heappush(max_heap, -1 * current_sum)
    top_3 = 0
    counter = 3
    while counter > 0 and max_heap:
        top_3 += -1 * heapq.heappop(max_heap)
        counter -= 1
    return top_3


lines = open("../input.txt").read().splitlines()
print(find_top_3_elves_with_most_calories(lines))
