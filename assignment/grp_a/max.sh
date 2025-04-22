read -p "Enter three Numbers: " a b c

if [ $a -gt $b ] && [ $a -gt $c ]; then
    max=$a
elif [ $b -gt $a ] && [ $b -gt $c ]; then
    max=$b
else
    max=$c
fi

echo "The maximum number is: $max"

