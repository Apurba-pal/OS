def sjf(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    completion_time = 0
    results = []

    while processes:
        available = [p for p in processes if p[1] <= completion_time]
        if not available:
            completion_time = processes[0][1]
            continue
        process = min(available, key=lambda x: x[2])
        processes.remove(process)
        pid, arrival_time, burst_time = process
        start_time = max(completion_time, arrival_time)
        completion_time = start_time + burst_time
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        results.append([pid, arrival_time, burst_time, waiting_time, turnaround_time,completion_time])

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for row in results:
        print(f"P{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}")

if __name__ == "__main__":
    print("SJF Scheduling Algorithm (Non-Preemptive)\n")

    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process P{i}: "))
        burst_time = int(input(f"Enter burst time for process P{i}: "))
        processes.append([i, arrival_time, burst_time])

    sjf(processes)
