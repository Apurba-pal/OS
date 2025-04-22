read -p "Enter the number of terms: " n

a=0
b=1

echo "Fibonacci Series:"
echo -n "$a "

if [ $n -gt 1 ]
then
    echo -n "$b "
fi

count=2
while [ $count -lt $n ]
do
    c=$((a + b))
    echo -n "$c "
    a=$b
    b=$c
    count=$((count + 1))
done

echo