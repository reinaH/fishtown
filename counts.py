# Instructions:
#
#   Implement each of the functions below to satisfy the problem, considering
#   the following:
#
#     1. does your solution work?
#     2. is your code clear and concise? is it readable?
#     3. is your code performant?
#
#   When you are done, upload your code to Github and send a link to
#   connor@fishtownanalytics.com.

import sys
import random

pool = []
minval = sys.maxsize
sumval = 0
count = 0
counts = {}
modek = 0
modev = 0

def process(i):
    """
    process() takes a single integer as an argument and does
    some background processing on it.

    process() should execute in constant time.
    """
    global pool, minval, sumval, count, counts, modev, modek

    pool.append(i)

    # running values to access average in constant time
    sumval += i
    count += 1

    # keep track of min
    if i < minval:
        minval = i

    # keep track of mode values to access in constant time below.
    # bc of how this is is written mode will return the first mode it comes
    # across in the event that you have multiple modes. here you have a
    # trade off- to access mode in constant time the code would not
    # parallelize well. would have to use threading or multiprocessing lib.
    if len(counts) == 0:
        modek = i
        modev = 1
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
        if counts[i] > modev:
            modek = i
            modev = counts[i]


def min():

    """
    min() returns the minimum of all of the integers passed
    to process() so far.

    min() should execute in constant time.
    """
    if len(pool) > 0:
        return (minval)


def avg():
    """
    avg() returns the average of all of the integers passed
    to process() so far.

    avg() should execute in constant time.
    """
    if len(pool) > 0:
        return round(sumval/count, 2)


def mode():
    """
    mode() returns the mode (most frequently occurring) of
    all of the integers passed to process() so far.

    what's the execution time of mode? can mode() run in constant time?
    """

    # process(i) keeps track of mode as you pass values,
    # otherwise this would be O(n). mode is accessed in constant
    # time bc dictionary lookups are generally constant.
    if len(counts) > 0:
        return (counts[modek])


def median():
    """
    median() returns the median (50th percentile) of
    all of the integers passed to process() so far.

    what's the big-O execution time of median()?
    """

    # funcs below come from source: https://rcoh.me/posts/linear-time-median-finding/

    # big o execution for this is O(n). the median of median methods
    # does not require you to sort the list- which would have put
    # you at O(nlogn).
    if len(pool) > 0:
        return (quickselect_median(pool))


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


process(1)
process(2)
process(2)
process(4)


print(min())  # should print "1"
print(avg())  # should print "2.25"
print(mode())  # should print "2"
print(median())  # should print "2"
