# WASP to develop a grade card where following grade will be calculated
# 91 - 100 → O

# 81 - 90 → A+

# 71 - 80 → A

# 61 - 70 → B+

# 51 - 60 → B

# 41 - 50 → C+

# 35 - 40 → C

# Less than 35 →


get_grade() {
    case $1 in
        100|9[0-9]) echo "Grade: A+" ;;
        8[0-9]) echo "Grade: A" ;;
        7[0-9]) echo "Grade: B" ;;
        6[0-9]) echo "Grade: C" ;;
        5[0-9]) echo "Grade: D" ;;
        4[0-9]) echo "Grade: E (Pass)" ;;
        [0-3][0-9]) echo "Grade: F (Fail)" ;;
        *) echo "Invalid average marks!" ;;
    esac
}

# Function to check if input is a valid number between 0 and 100
is_valid_marks() {
    echo "$1" | grep -qE '^[0-9]+$' && [ "$1" -ge 0 ] && [ "$1" -le 100 ]
}

# Prompt user for marks in three subjects
read -p "Enter marks for Subject 1 (0-100): " sub1
read -p "Enter marks for Subject 2 (0-100): " sub2
read -p "Enter marks for Subject 3 (0-100): " sub3

# Validate inputs
if ! is_valid_marks "$sub1" || ! is_valid_marks "$sub2" || ! is_valid_marks "$sub3"; then
    echo "Error: Please enter valid numeric marks between 0 and 100."
    exit 1
fi

# Calculate average
average=$(( (sub1 + sub2 + sub3) / 3 ))

# Display results
echo "Average Marks: $average"
get_grade "$average"