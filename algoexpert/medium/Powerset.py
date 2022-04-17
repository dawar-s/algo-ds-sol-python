def powerset(array):
    subsets = [[]]
    for item in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [item])
    return subsets


print(powerset([1, 2, 3]))
