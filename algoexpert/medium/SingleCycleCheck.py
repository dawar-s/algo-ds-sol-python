def hasSingleCycle(array):
    visited = 0
    idx = 0
    while visited < len(array):
        if visited > 0 and idx == 0:
            return False
        visited += 1
        idx = get_next_idx(idx, array)

    return idx == 0


def get_next_idx(idx, array):
    x = (idx + array[idx]) % len(array)
    return x if x >= 0 else x + len(array)


a = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(a))
