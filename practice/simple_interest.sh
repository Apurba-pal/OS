echo "enter the values"
read -p "principle: " p
read -p "rate: " r
read -p "time: " t

# calculate simple interest
si=$(echo "scale=2; (($p * $r * $t) / 100)" | bc)
echo $si