def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    current = intervals[0]
    result.append(current)

    for next_interval in intervals:
        _, current_end = current
        next_start, next_end = next_interval

        if current_end >= next_start:
            current[1] = max(current_end, next_end)
        else:
            current = next_interval
            result.append(current)

    return result
