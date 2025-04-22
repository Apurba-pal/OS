
echo "Simple Calculator"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "5. Exit"

while true
do
    read -p "Enter your choice (1-5): " choice

    case $choice in
        1)
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            echo "Result: $((num1 + num2))"
            ;;
        2)
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            echo "Result: $((num1 - num2))"
            ;;
        3)
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            echo "Result: $((num1 * num2))"
            ;;
        4)
            read -p "Enter first number: " num1
            read -p "Enter second number: " num2
            if [ $num2 -ne 0 ]; then
                echo "Result: $(bc -l <<< "scale=2; $num1 / $num2")"
            else
                echo "Error: Division by zero is not allowed."
            fi
            ;;
        5)
            exit 0
            ;;
        *)
            echo "Invalid choice. Please choose a valid option."
            ;;
    esac
done