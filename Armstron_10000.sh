#!/bin/bash

# Function to check if a number is an Armstrong number
is_armstrong() {
    local num=$1
    local sum=0
    local temp=$num
    local n=${#num}
    
    while [ $temp -gt 0 ]; do
        local digit=$((temp % 10))
        sum=$((sum + digit**n))
        temp=$((temp / 10))
    done
    
    if [ $sum -eq $num ]; then
        return 0
    else
        return 1
    fi
}

# Print all Armstrong numbers within 10000
for ((num=1; num<=10000; num++)); do
    if is_armstrong $num; then
        echo $num
    fi
done


