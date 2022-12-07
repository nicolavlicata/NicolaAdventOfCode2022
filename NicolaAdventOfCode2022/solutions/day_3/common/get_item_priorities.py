def get_item_priorities(common_items):
    item_priorities = 0
    for common_item in common_items:
        if common_item.islower():
            item_priorities += ord(common_item) - 96
        else:
            item_priorities += ord(common_item) - 38
    return item_priorities
