
# Function to calculate average score and average with handicap
def calculateBowling(game1, game2, game3, handicap):

    # Calculate the average of the three games
    averageScore = (game1 + game2 + game3) / 3

    # Calculate the average score with handicap
    averageWithHandicap = averageScore + handicap

    # Return both values
    return averageScore, averageWithHandicap


# Get bowler information from the user
lastName = input("Enter bowler's last name: ")
game1 = int(input("Enter first game score: "))
game2 = int(input("Enter second game score: "))
game3 = int(input("Enter third game score: "))
handicap = int(input("Enter bowling handicap: "))

# Call the function and receive both returned values
averageScore, averageWithHandicap = calculateBowling(game1, game2, game3, handicap)

# Display the results
print("\nBowling Score Information")
print("Last Name:", lastName)
print("Average Score:", format(averageScore, ".2f"))
print("Average Score with Handicap:", format(averageWithHandicap, ".2f"))
