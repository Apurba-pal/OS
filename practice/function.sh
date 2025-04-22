read -p "enter a number: " num
function fact(){
    local n=$1
    if (( n == 0 )); then
        echo 1
    else
        echo $(($n * $(fact $((n-1)))))
    fi
}

fact $num