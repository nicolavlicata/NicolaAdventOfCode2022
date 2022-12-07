from day_3.common.get_item_priorities import get_item_priorities
from utils.timer import timer_func

@timer_func
def sum_of_common_rucksack_items(rucksacks):
    common_items = []
    for rucksack in rucksacks:
        seen = set()
        mid_point = len(rucksack) // 2
        for idx, item in enumerate(rucksack):
            if idx < mid_point:
                seen.add(item)
            else:
                if item in seen:
                    common_items.append(item)
                    break
    return get_item_priorities(common_items)


lines = open("../input.txt").read().splitlines()
print(sum_of_common_rucksack_items(lines))
