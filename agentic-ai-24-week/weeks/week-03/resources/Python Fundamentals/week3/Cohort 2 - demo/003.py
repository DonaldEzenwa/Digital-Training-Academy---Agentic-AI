# You are a seller of smart phones and want to check
# the eligibility of a customer to get a 105 discount.
# If the total bill of the customer is more than $2000,
# you offer them a 10% discount flat.


p_name = input("Brand Name: ")
p_model = input("Phone Model: ")
p_storage = input("Storage Option: ")
p_price  = float(input("Per Unit Price: "))
qty = int(input("Units Sold: "))
dis_rate = 0.0 # 0.10 is same as 10%
discount = 0
g_amnt = p_price * qty
n_amnt = g_amnt

"""
if condition-is-true:
    do-this
    and-this
    and-this
else:
    do-that
    and-that
"""

if g_amnt > 2000:
    dis_rate = 0.10
    discount = g_amnt * dis_rate
    n_amnt = g_amnt - discount

print(f"""
Product: {p_name} {p_model}
Option: {p_storage}
Price: ${p_price}
Units: {qty}
Gross Amount: ${g_amnt}
Discount Rate: {dis_rate *100}%
Discount: ${discount}
Pay Amount: ${n_amnt}
""")
