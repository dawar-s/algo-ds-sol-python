def subarraySort(array):
    min_ascending_anomaly_number = float('inf')
    max_descending_anomaly_number = float('-inf')
    i, j = 1, len(array) - 2

    while i < len(array) and j > - 1:
        if array[i] < array[i - 1]:
            min_ascending_anomaly_number = min(array[i], min_ascending_anomaly_number)
        if array[j] > array[j + 1]:
            max_descending_anomaly_number = max(array[j], max_descending_anomaly_number)
        i += 1
        j -= 1

    if min_ascending_anomaly_number == float('inf'):
        return [-1, -1]

    subarray_left_idx, subarray_right_idx = 0, len(array) - 1

    while array[subarray_left_idx] <= min_ascending_anomaly_number:
        subarray_left_idx += 1
    while array[subarray_right_idx] >= max_descending_anomaly_number:
        subarray_right_idx -= 1

    return [subarray_left_idx, subarray_right_idx]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))