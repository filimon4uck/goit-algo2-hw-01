def min_max_recursivety(lst, index=0, max_val=None, min_val=None):
    if index == len(lst):
        return (min_val, max_val)
    cur = lst[index]
    if not max_val or max_val < cur:
        max_val = cur
    if not min_val or min_val > cur:
        min_val = cur
    return min_max_recursivety(lst, index + 1, max_val, min_val)


def main():
    lst1 = [3]
    lst2 = [3, 4, 34, 545, 656, 7]

    print(min_max_recursivety(lst1))
    print(min_max_recursivety(lst2))


if __name__ == "__main__":
    main()
