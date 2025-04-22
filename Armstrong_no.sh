read -p "Enter a number: " num

original_num=$num
sum=0

num_digits=${#num}

while [ "$num" -gt 0 ]; do
    digit=$((num % 10))
    sum=$((sum + digit**num_digits))
    num=$((num / 10))
done

if [ "$sum" -eq "$original_num" ]; then
    echo "$original_num is an Armstrong number."
else
    echo "$original_num is not an Armstrong number."
fi
