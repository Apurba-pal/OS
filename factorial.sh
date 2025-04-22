read -p "Enter a number: " num

fact=1

if [ "$num" -lt 0 ]; then
    echo "Factorial is not defined for negative numbers."
    exit 1
fi

for ((i = 1; i <= num; i++)); do
    fact=$((fact * i))
done

echo "Factorial of $num is $fact."
