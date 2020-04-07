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

    i = 0
    j = 0
    # Repeat until one list is empty
    while len(items1) > i and len(items2) > j:
        # Find minimum item in both lists and append it to new list
        if items1[i] < items2[j]:
            items3.append(items1[i])
            i += 1
        else:
            items3.append(items2[j])
            j += 1
    # Append remaining items in non-empty list to new list
    items3.extend(items1[i:])
    items3.extend(items2[j:])

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
    `[low...high]` by choosing a pivot (picking the last element) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) since we go through elements between low and high 
    which can bet the first and last element 
    Memory usage: O(1) since it is done in place"""
    left = low - 1
    #  Choose a pivot any way and document your method in docstring above
    pivot = items[high]
    # Loop through all items in range [low...high]
    for j in range(low, high):
    # Move items less than pivot into front of range [low...p-1]
        if items[j] < pivot:
            left += 1
            # Move items greater than pivot into back of range [p+1...high]
            items[left], items[j] = items[j], items[left]
    # Move pivot item into final position [p] and return index p
    items[left + 1], items[high] = items[high], items[left+1]
    return left+1

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(nlogn) when partition always picks middle element
    Worst case running time: O(n^2) when partition always picks greates or smallest
    element
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    if low == None:
        low = 0
    if high == None:
        high = len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        partition_index = partition(items, low, high)
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, partition_index - 1)
        quick_sort(items, partition_index + 1, high)

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