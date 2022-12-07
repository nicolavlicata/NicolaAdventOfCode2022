from day_3.common.get_item_priorities import get_item_priorities
from utils.timer import timer_func


@timer_func
def sum_of_common_items_in_elf_groups(rucksacks):
    common_items = []
    for i in range(0, len(rucksacks), 3):
        rucksack1 = set(rucksacks[i])
        rucksack2 = set(rucksacks[i+1])
        rucksack3 = set(rucksacks[i+2])
        common_item = rucksack1.intersection(rucksack2).intersection(rucksack3)
        common_items.append(common_item.pop())
    return get_item_priorities(common_items)


lines = open("../input.txt").read().splitlines()
print(sum_of_common_items_in_elf_groups(lines))
