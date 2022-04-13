def taskAssignment(k, tasks):
    task_duration_with_indices = []
    for i, task in enumerate(tasks):
        task_duration_with_indices.append([i, task])
    task_duration_with_indices = sorted(task_duration_with_indices, key=lambda x: x[1])

    paired_tasks = []
    i, j = 0, len(tasks) - 1
    while i < j:
        paired_tasks.append([task_duration_with_indices[i][0], task_duration_with_indices[j][0]])
        i += 1
        j -= 1

    return paired_tasks


print(taskAssignment(3, [1, 3, 5, 3, 1, 4]))

