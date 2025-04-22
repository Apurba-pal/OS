n = int(input('Enter number of processes: '))
at = list(map(int, input(f'Enter arrival times for {n} processes: ').split()))
bt = list(map(int, input(f'Enter burst times for {n} processes: ').split()))
tq = int(input('Enter time quantum: '))

remaining_bt = bt.copy()
t = 0
wt = [0] * n
tat = [0] * n

while True:
    done = True
    for i in range(n):
        if remaining_bt[i] > 0:
            done = False
            if remaining_bt[i] > tq:
                t += tq
                remaining_bt[i] -= tq
            else:
                t += remaining_bt[i]
                wt[i] = t - bt[i] - at[i]
                remaining_bt[i] = 0
    if done:
        break

for i in range(n):
    tat[i] = bt[i] + wt[i]

print('Process	Burst Time	Waiting Time	Turnaround Time')
for i in range(n):
    print(f'{i+1}	{bt[i]}		{wt[i]}		{tat[i]}')

avg_wt = sum(wt) / n
avg_tat = sum(tat) / n
print(f'Average Waiting Time: {avg_wt}')
print(f'Average Turnaround Time: {avg_tat}')