
# Function to calculate commission and next year's target
def calculateSales(sales):

    # Determine commission percentage based on sales
    if sales > 100000:
        commissionRate = 0.10
    else:
        commissionRate = 0.05

    # Calculate the commission amount
    commission = sales * commissionRate

    # Calculate next year's target at 5% of sales
    nextYearTarget = sales * 0.05

    # Return both values
    return commission, nextYearTarget


# Get salesperson information from the user
lastName = input("Enter salesperson's last name: ")
sales = float(input("Enter sales amount: "))

# Call the function and receive both returned values
commission, nextYearTarget = calculateSales(sales)

# Display the sales report
print("\nSales Report")
print("Salesperson Last Name:", lastName)
print("Commission: $", format(commission, ".2f"))
print("Next Year's Target: $", format(nextYearTarget, ".2f"))
