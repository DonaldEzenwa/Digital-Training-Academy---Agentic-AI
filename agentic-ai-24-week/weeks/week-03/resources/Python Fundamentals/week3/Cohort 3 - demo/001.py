p_name = "iPhone"
p_model = "17 Pro Max"
p_price = 1899
qty = 5
amount = p_price * qty

# print(p_name) - comment, not executed by Python

# iPhone 17 Pro Max is available for $1899
# p_name p_model is available for $p_price

print(f"{p_name} {p_model} is available for ${p_price}.")
# f"..." - formatted string for putput

# print(f"Sold {qty} units for ${amount}.")
print(f"{qty} units sold for ${p_price * qty}.")
