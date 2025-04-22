check_character_type() {
    char=$1
    if [[ $char =~ [A-Z] ]]; then
        echo "Uppercase letter"
    elif [[ $char =~ [a-z] ]]; then
        echo "Lowercase letter"
    elif [[ $char =~ [0-9] ]]; then
        echo "Numeric value"
    else
        echo "Special symbol"
    fi
}

read -p "Enter a character: " input_char

result=$(check_character_type "$input_char")
echo "The character '$input_char' is a $result."
