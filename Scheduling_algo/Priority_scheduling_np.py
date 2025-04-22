def priority_scheduling(processes):
        processes.sort(key=lambda x: x[3])  # Sort by priority
        completion_time = 0
        results = []
    
        for process in processes:
            pid, burst_time, arrival_time, priority = process
            start_time = max(completion_time, arrival_time)
            completion_time = start_time + burst_time
            turnaround_time = completion_time - arrival_time
            waiting_time = turnaround_time - burst_time
            results.append([pid, burst_time, arrival_time, priority, waiting_time, turnaround_time, completion_time])
    
        print("Process\tBurst Time\tArrival Time\tPriority\tWaiting Time\tTurnaround Time\tCompletion Time")
        for row in results:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")
        
        total_tat = sum(row[5] for row in results)  # Sum of Turnaround Times
        total_wt = sum(row[4] for row in results)  # Sum of Waiting Times
        avg_tat = total_tat / len(results)  # Average Turnaround Time
        avg_wt = total_wt / len(results)  # Average Waiting Time

        print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
        print(f"Average Waiting Time: {avg_wt:.2f}")
    
    # Example usage:
processes = [
        [1, 10, 0, 3],  # PID, Burst Time, Arrival Time, Priority
        [2, 1, 2, 1],
        [3, 2, 3, 4],
        [4, 1, 5, 2]
    ]
priority_scheduling(processes)