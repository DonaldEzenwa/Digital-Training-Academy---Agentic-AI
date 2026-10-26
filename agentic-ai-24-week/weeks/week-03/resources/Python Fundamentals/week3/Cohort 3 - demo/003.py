# if the sales is between $1000 and $2000, then allow a 5% discount
# else if the sales is between $2000 and $4000, then allow a 10% discount
# else if the sales is above $4000, then allow a 15% discount



p_name = input("Phone brand: ")
p_model = input("Phone model: ")
p_price = float(input("Unit price in $: "))
qty = int(input("Quantity sold: "))
g_amnt = p_price * qty
d_rate = 0.0    # discount rate set at 0% (0.0) for sales less than  $1000.

"""
if condition-is-true:
    do-this
else:
    do-that


if condition-is-true:
    do-this
elif condition-2-is-true:
    do-that-1
elif condition-3-is-true:
    do-that-2
else:
    do-that-3
"""

if g_amnt >= 1000 and g_amnt < 2000:
    d_rate = 0.05 # 5% is 0.05
elif g_amnt >= 2000 and g_amnt < 4000:
    d_rate = 0.10 # 10% is 0.10
elif g_amnt >= 4000:
    d_rate = 0.15 # 15% is 0.15


disc = g_amnt * d_rate
n_amnt = g_amnt - disc


print(f"Proudct: {p_name} {p_model}")
print(f"Price: {p_price}")
print(f"Gross Amount: ${g_amnt}")
print(f"Discount: ${disc}")
print(f"Net Amount: ${n_amnt}")
