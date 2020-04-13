#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == "__main__":
    num = [2, 2, 5, 3, 1]
    counting_sort(num)
    print(num)