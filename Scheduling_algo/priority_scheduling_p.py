def preemptive_priority_scheduling(processes):     

    n = len(processes)
    processes.sort(key=lambda x: x[2])  # Sort by arrival time
    remaining_burst = [p[1] for p in processes]
    complete, time = 0, 0
    completion_time, waiting_time, turnaround_time = [0] * n, [0] * n, [0] * n

    while complete < n:
        idx = min((i for i in range(n) if processes[i][2] <= time and remaining_burst[i] > 0),
                  default=-1, key=lambda i: processes[i][3])

        if idx != -1:
            remaining_burst[idx] -= 1
            if remaining_burst[idx] == 0:
                complete += 1
                completion_time[idx] = time + 1
                turnaround_time[idx] = completion_time[idx] - processes[idx][2]
                waiting_time[idx] = turnaround_time[idx] - processes[idx][1]
        time += 1

    print("PID\tBT\tAT\tPR\tWT\tTAT\tCT")
    for i, (pid, bt, at, pr) in enumerate(processes):
        print(f"{pid}\t{bt}\t{at}\t{pr}\t{waiting_time[i]}\t{turnaround_time[i]}\t{completion_time[i]}")

    avg_tat = sum(turnaround_time) / n  # Average Turnaround Time
    avg_wt = sum(waiting_time) / n  # Average Waiting Time

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


processes = [[0, 6, 2, 1], [1, 8, 1, 2], [2, 7, 3, 3], [3, 3, 4, 2]]
preemptive_priority_scheduling(processes)