def qsort(a):
    """Quicksort altgorithm - however this is not the best way because pivot is not random"""
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [ i for i in a[1:] if i <= pivot ]
        more = [ i for i in a[1:] if i >  pivot ]

        return qsort(less) + [pivot] + qsort(more)

print qsort([3, 2, 5, 1, 0])
