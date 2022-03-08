# O(n) time | O(10 space
def longestPeak(array):
    if len(array) < 3:
        return 0
    i = 1
    longest_peak = 0
    while i < len(array) - 1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue
        current_peak = 3
        left = i - 1
        while left > 0 and array[left] > array[left - 1]:
            left -= 1
            current_peak += 1
        right = i + 1
        while right < len(array) - 1 and array[right] > array[right + 1]:
            right += 1
            current_peak += 1
        longest_peak = current_peak if current_peak > longest_peak else longest_peak
        i = right

    return longest_peak
