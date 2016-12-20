import time

def binary_search(list, item):
    """Return the index of the item in a sorted list. This is a O(log n) algorithm."""

    low = 0
    high = len(list) - 1

    i = 1
    while low <= high:
        mid = (high + low) / 2
        guess = list[mid]   # don't forget this indirection!

        # debug info
        print "iteration", i, "-", "low index", low, "high index", high, "middle index", mid
        i = i + 1
        time.sleep(2)

        if guess == item:
            return mid
        elif guess < item:  # the guess was too low
            low = mid + 1
        elif guess > item:  # the guess was too high
            high = mid - 1
        else:               # we should never get here
            print "something's wrong"
            exit(1)

    # the item is not in the list
    return None

list = range(1, 33)
item =  27
print "Searching index of item", item, "in", list
print
index = binary_search(list, item)
print
print "Items' index is", index