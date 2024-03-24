def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent/100)
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price == original_price:
    print("No discount applied. Final price: $", final_price)
else:
    print(f"Discount applied. Final price after {discount_percentage}% discount: ${final_price:.2f}")