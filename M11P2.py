
# Function to calculate total points and average exam score
def calculateScores(exam1, exam2, exam3):

    # Calculate total exam points
    totalPoints = exam1 + exam2 + exam3

    # Calculate average exam score
    average = totalPoints / 3

    # Return both values
    return totalPoints, average


# Get student information from the user
lastName = input("Enter student's last name: ")
exam1 = float(input("Enter first exam score: "))
exam2 = float(input("Enter second exam score: "))
exam3 = float(input("Enter third exam score: "))

# Call the function and receive both returned values
totalPoints, average = calculateScores(exam1, exam2, exam3)

# Display the results
print("\nStudent Exam Information")
print("Last Name:", lastName)
print("Total Points:", format(totalPoints, ".2f"))
print("Average Exam Score:", format(average, ".2f"))

