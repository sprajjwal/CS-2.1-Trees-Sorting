#!python

from sorting_recursive import merge_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(max(n) + n) Why and under what conditions?
    Memory usage: O(n) since we make a new array with all items."""
    if len(numbers) < 2:
        return
    # Find range of given numbers (minimum and maximum integer values)
    minm = min(numbers)
    maxm = max(numbers)
    range_num = maxm - minm + 1

    # Create list of counts with a slot for each number in input range
    array = [0] * range_num

    # Loop over given numbers and increment each number's count
    for num in numbers:
        array[num - minm] += 1
    # Loop over counts and append that many numbers into output list
    # Improve this to mutate input instead of creating new output list
    i, j = 0, 0
    while i < len(numbers):
        while array[j] < 1:
            j += 1
        numbers[i] = minm + j
        array[j] -= 1
        i += 1

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n.logn) since merge sort is called
    Memory usage: O(n) since we make an extra 2d array for items"""
    # Find range of given numbers (minimum and maximum values)
    if len(numbers) < 2:
        return
    minm = min(numbers)
    maxm = max(numbers)
    bucket_range = (maxm - minm) // num_buckets + 1

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for item in numbers:
        index = (item - minm) // bucket_range
        buckets[index].append(item)

    # Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(buckets)):
        merge_sort(buckets[i])

    # Improve this to mutate input instead of creating new output list

    i = 0
    for bucket in buckets:
        for item in bucket:
            numbers[i] = item
            i += 1


if __name__ == "__main__":
    num = [2, 2, 0, 5, 3, 1]
    bucket_sort(num)
    print(num)