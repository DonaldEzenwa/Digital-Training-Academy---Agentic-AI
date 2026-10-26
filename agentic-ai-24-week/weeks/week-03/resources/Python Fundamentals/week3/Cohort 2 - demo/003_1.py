"""
You are a seller of smart phones and want to check
the eligibility of a customer to get a 105 discount.
If the total bill of the customer is:
1)IF more than $4000, give a discount of 10%
2)ELSE IF more than 2000 but up to 4000, then a discount of 7.5%
3)ELSE IF more than 500 but up to 2000, then a discount of 2.5%
4)ELSE up to 500, no discount 
"""


p_name = input("Brand Name: ")
p_model = input("Phone Model: ")
p_storage = input("Storage Option: ")
p_price  = float(input("Per Unit Price: "))
qty = int(input("Units Sold: "))
dis_rate = 0.0 # 0.10 is same as 10%
g_amnt = p_price * qty

"""
if condition1-is-true:
    do-this
elif condition2-is-true:
    do-that1
elif condition3-is-true:
    do-that2
else:
    do-default
"""

if g_amnt > 4000:
    dis_rate = 0.10
elif g_amnt > 2000 and g_amnt <= 4000:
    dis_rate = 0.075
elif g_amnt > 500 and g_amnt <= 2000:
    dis_rate = 0.025

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
