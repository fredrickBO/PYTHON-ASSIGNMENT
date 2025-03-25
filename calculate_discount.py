def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    if discount_percent >= 20:
        return final_price
    else:
        return price
    
calculate_discount(100, 30)

price = float(input("Enter the price: "))
discount_percent = int(input("Enter the discount percent: "))
calculate_discount(price, discount_percent)
