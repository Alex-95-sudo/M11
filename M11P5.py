
# Initialize global variables
total = 0
tax = 0

# Function to calculate total and sales tax
def calculateTotal(quantity, unitPrice):

    # Declare global variables
    global total, tax

    # Calculate the total price
    total = quantity * unitPrice

    # Calculate 7% sales tax
    tax = total * 0.07


# Get item information from the user
quantity = int(input("Enter quantity: "))
unitPrice = float(input("Enter unit price: "))

# Call the function to calculate total and tax
calculateTotal(quantity, unitPrice)

# Display the results in the main program
print("\nSales Information")
print("Quantity:", quantity)
print("Unit Price: $", format(unitPrice, ".2f"))
print("Total: $", format(total, ".2f"))
print("Sales Tax: $", format(tax, ".2f"))
