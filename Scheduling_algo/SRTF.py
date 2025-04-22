def srtf(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    completion_time = 0
    results = []
    remaining_processes = {p[0]: p[2] for p in processes}  #creates a dictionary where key value pairs are ... PID -> Remaining Burst Time

    while remaining_processes:
        available = [p for p in processes if p[1] <= completion_time and p[0] in remaining_processes]
        if not available:
            completion_time += 1
            continue
        process = min(available, key=lambda x: remaining_processes[x[0]])
        pid, arrival_time, _ = process
        remaining_processes[pid] -= 1
        completion_time += 1
        if remaining_processes[pid] == 0:
            del remaining_processes[pid]
            turnaround_time = completion_time - arrival_time
            waiting_time = turnaround_time - process[2]
            results.append([pid, arrival_time, process[2], waiting_time, turnaround_time, completion_time])

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for row in results:
        print(f"P{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}")

if __name__ == "__main__":
    print("SRTF \n")
    processes = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process P{i}: "))
        burst_time = int(input(f"Enter burst time for process P{i}: "))
        processes.append([i, arrival_time, burst_time])
    srtf(processes)