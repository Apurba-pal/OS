#!/bin/bash

# Function to simulate a task (thread)
task() {
    echo "Task $1 started..."
    sleep $((RANDOM % 5 + 1))  # Simulating work with sleep
    echo "Task $1 completed!"
}

# Number of threads
THREADS=5

# Loop to create multiple threads
for ((i=1; i<=THREADS; i++)); do
    task "$i" &  # Run task in background (acts as a thread)
done

# Wait for all background processes to complete
wait

echo "All tasks completed!"
