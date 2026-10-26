p_name = input("Brand Name: ")
p_model = input("Phone Model: ")
p_storage = input("Storage Option: ")
p_price  = float(input("Per Unit Price: "))
qty = int(input("Units Sold: "))


# {qty} units sold of {p_name} {p_model} with {p_storage} option at ${p_price}
# 3 units sold of iPhone 17 Pro Max with 512GB option at $1899

print(f"{qty} units sold of {p_name} {p_model} with {p_storage} option at ${p_price}")


# print(f"...") - here the 'f' represents formatted output

"""
Product: iPhone 17 Pro Max
Option: 512GB
Price: $1899
Units: 03
Amount: $5697
"""

"""
Product: {p_name} {p_model}
Option: {p_storage}
Price: ${p_price}
Units: {qty}
Amount: ${p_price * qty}
"""

print(f"""
Product: {p_name} {p_model}
Option: {p_storage}
Price: ${p_price}
Units: {qty}
Amount: ${p_price * qty}
""")
