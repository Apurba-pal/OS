read -p  "Enter number: " a

rim=$((a&1))

if [ $rim -eq 0 ]; then
echo $a is even
else
echo $a is odd
fi