def bubble_sort(items):
    index = len(items) - 1
    swapped = True
    print(items)
    while swapped:
        swapped = False
        for i in range(index):
            left = items[i]
            right = items[i+1]
            if left > right:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
    return items

print(bubble_sort([3,5,1,6,6,8,4,2,4,5,8,9,4,23,0]))

