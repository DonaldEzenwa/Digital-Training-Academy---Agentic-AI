product_name = input("Phone model name: ")
product_price = int(input("per unit price: "))
qty = 4

total_amount = product_price * qty

# {qty} units of {product_name} sold at ${product_price} for ${total_amount}
# 4 units of iPhone sold at $1599 for $5996

print(f"{qty} units of {product_name} sold at ${product_price} for ${total_amount}")
