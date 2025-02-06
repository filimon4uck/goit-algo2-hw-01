def quick_select(lst, k):
    if not lst or k < 0 or k >= len(lst):
        return None

    pivot = lst[len(lst) // 2]

    less = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    greater = [x for x in lst if x > pivot]

    if k < len(less):
        return quick_select(less, k)
    elif k < len(less) + len(middle):
        return pivot
    else:
        return quick_select(greater, k - len(less) - len(middle))


print(quick_select([8, 7, 6, 5, 6, 6, 6, 7, 4, 5, 2, 1], 4))
print(quick_select([1], -1))
print(quick_select([], 2))
