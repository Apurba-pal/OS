read -p "Enter Two NUmbers: " a b

echo "Before swapping: a = $a, b = $b"

a=$((a+b))
b=$((a-b))
a=$((a-b))

echo "After swapping: a = $a, b = $b"