#!python
from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(m) where m is the length of the shorter list
    Memory usage: O(m+n) where m and n are the length of the lists"""
    if len(items1) == 0:
        return items2
    if len(items2) == 0:
        return items1
    items3 = []

    # Repeat until one list is empty
    while len(items1) > 0 and len(items2) > 0:
        # Find minimum item in both lists and append it to new list
        if items1[0] < items2[0]:
            items3.append(items1.pop(0))
        else:
            items3.append(items2.pop(0))
    # Append remaining items in non-empty list to new list
    items3.extend(items1)
    items3.extend(items2)

    return items3



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n^2) since insertion sort takes O(n^2) for each n/2 halves
    and then merging and updating takes O(n).
    Memory usage: O(n^2) merging function returns a new variable after merging"""
    mid = len(items) // 2 

    # Split items list into approximately equal halves
    left = items[:mid]
    right = items[mid:]

    #  Sort each half using any other sorting algorithm
    insertion_sort(left) 
    insertion_sort(right) 
    # Merge sorted halves into one list in sorted order
    merged = merge(left, right)
    items[:] = merged
    # for i in range(len(items)):
    #     items[i] = merged[i]

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n.logn) since merging takes O(n)
    Memory usage: O(n^2) merging function returns a new variable after merging"""
    # Check if list is so small it's already sorted (base case)
    if len(items) > 1:
        mid = len(items) // 2
        # Split items list into approximately equal halves
        left = items[:mid]
        right = items[mid:]

        # Sort each half by recursively calling merge sort
        merge_sort(left)
        merge_sort(right)

        merged = merge(left, right)
        items[:] = merged
        # for i in range(len(items)):
        #     items[i] = merged[i]


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":
    a = [1, 3, 6, 7, 9, 10]
    b = [1, 2, 2, 5, 6]
    c = [5, 8, 2, 6, 7, 7, 8, 2, 1, 8, 8, 6, 2, 7, 5, 8, 6, 6, 8, 8]
    # print(sorted(list(a + b)))
    # print(merge(a, b))
    print(sorted(list(c)))
    merge_sort(c)
    print(c)
    # print(merge_sort(c))