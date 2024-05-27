def binary_search(collection, item):
    l = 0
    h = len(collection) - 1

    while l < h:
        mid = (l+h) // 2
        guess = collection[mid]

        if guess == item:
            return mid
        elif guess < item:
            l = mid + 1
        else:
            h = mid - 1

    return -1
