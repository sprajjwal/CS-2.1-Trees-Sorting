#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because we iterate through the loop once
    Memory usage: O(1) because we check in place"""
    # Check that all adjacent items are in order, return early if so
    if len(items) < 2:
        return True
    for index in range(len(items) - 1):
        if items[index] > items[index + 1]: 
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) because we iterate over the whole loop once then 
    iterate over n-i items
    Memory usage: O(1) because it is in place."""
    if len(items) < 2:
        return 
    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order
    for i in range(len(items)):
        swapped = false
        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    # return items
    


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2)
    TODO: Memory usage: O(1)"""
    if len(items) < 2:
        return 
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        min = i
        for j in range(i, len(items)):
            # Find minimum item in unsorted items
            if items[min] > items[j]:
                min = j
        # Swap it with first unsorted item
        items[i], items[min] = items[min], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    for i in range(1, len(items)):
        # Take first unsorted item
        selected = items[i]
        # Insert it in sorted order in front of items
        move_to = i
        for j in range(i - 1, -1, -1):
            if items[j] > selected:
                items[j + 1] = items[j]
                move_to = j
            else:
                break
        items[move_to] = selected
                



if __name__ == "__main__": 
    assert is_sorted([(3, 5)]) is True
    assert is_sorted([(3, 'A')]) is True  # Single item
    assert is_sorted([('A', 3)]) is True  # Single item
    assert is_sorted([('A', 'B')]) is True  # Single item