# O(n) time | O(n) space
def largestRange(array):
    dic = {num: True for num in array}
    max_range = 1
    result = [array[0], array[0]]
    for num in array:
        left, right = num, num
        if not dic[num]:
            continue
        while left - 1 in dic:
            left -= 1
            dic[left] = False
        while right + 1 in dic:
            right += 1
            dic[right] = False
        if right - left + 1 > max_range:
            max_range = right - left + 1
            result = [left, right]

    return result
