
# Function to calculate discount amount and discounted price
def calculateDiscount(quantity, price, discountRate):

    # Calculate the total price
    totalPrice = quantity * price

    # Calculate the discount amount
    discountAmount = totalPrice * discountRate

    # Calculate the discounted price
    discountedPrice = totalPrice - discountAmount

    # Return both values
    return discountAmount, discountedPrice


# Get input from the user
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discountRate = float(input("Enter discount rate (as a decimal): "))

# Call the function and receive both returned values
discountAmount, discountedPrice = calculateDiscount(quantity, price, discountRate)

# Display the results
print("\nDiscount Information")
print("Quantity:", quantity)
print("Price: $", format(price, ".2f"))
print("Discount Amount: $", format(discountAmount, ".2f"))
print("Discounted Price: $", format(discountedPrice, ".2f"))
