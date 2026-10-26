p_name = input("Phone brand: ")
p_model = input("Phone model: ")
p_price = float(input("Unit price in $: "))
qty = int(input("Quantity sold: "))
amount = p_price * qty


print(f"{p_name} {p_model} is available for ${p_price}.")
print(f"{qty} units sold for ${p_price * qty}.")
