def optimalFreelancing(jobs):
    jobs.sort(key=lambda x: (x['payment']), reverse=True)
    counted = [False for _ in range(7)]
    payment = 0
    for i in range(len(jobs)):
        j = min(jobs[i]['deadline'] - 1, 6)
        while j >= 0 and counted[j]:
            j -= 1
        if j >= 0:
            payment += jobs[i]['payment']
            counted[j] = True

    return payment