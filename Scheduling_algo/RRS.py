def round_robin(processes, time_quantum):
    queue = processes[:]
    time = 0
    results = []
    burst_times = {p[0]: p[2] for p in processes}  # PID -> Original Burst Time

    while queue:
        process = queue.pop(0)
        pid, arrival_time, burst_time = process

        if arrival_time > time:
            time = arrival_time

        execution_time = min(burst_time, time_quantum)
        time += execution_time
        burst_time -= execution_time

        if burst_time > 0:
            queue.append([pid, arrival_time, burst_time])
        else:
            turnaround_time = time - arrival_time
            waiting_time = turnaround_time - burst_times[pid]
            results.append([pid, arrival_time, burst_times[pid], waiting_time, turnaround_time, time])

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for row in results:
        print(f"P{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}")

if __name__ == "__main__":
    print("Round Robin Scheduling Algorithm")
    processes = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process P{i}: "))
        burst_time = int(input(f"Enter burst time for process P{i}: "))
        processes.append([i, arrival_time, burst_time])

    time_quantum = int(input("Enter the time quantum: "))
    round_robin(processes, time_quantum)