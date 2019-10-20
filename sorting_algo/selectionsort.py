def selection_sort(listy):
    for i in range(len(listy) - 1):
        minimumpos = i
        for j in range(i, len(listy)):
            if listy[j] < listy[minimumpos]:
                minimumpos = j
        listy[i], listy[minimumpos] = listy[minimumpos], listy[i]
    return listy

l = [4,56,34,3,2,54,6,78,8,6,5,433,23,45,67,8,0]
print(selection_sort(l))
