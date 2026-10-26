'''
If the total sales in under $1000, there is  no discount
Else if the total sales is between 1000 and 2000, then the discount is at 7.5%
Else if the total sales is between 2000 and 4000, then the discount is at 12.5%
Else if the total sales is above 4000, then the discount is at 17.5%
'''

no_products = int(input("how many products?"))

for i in range(0, no_products): # no is 3: 0, 1, 2

    p_name = input(f"{i} product name? ")
    p_price = float(input("price per unit ($)? "))
    qty = int(input("units sold? "))
    amnt = p_price * qty
    d_rate = 0.0


    if amnt < 1000:
        d_rate = 0.0
    elif amnt >= 1000 and amnt < 2000:
        d_rate = 0.075 # 0.1 is 10%
    elif amnt >= 2000 and amnt < 4000:
        d_rate = 0.125
    elif amnt >= 4000:  # else: would also do
        d_rate = 0.175

    disc = amnt * d_rate
    n_amnt = amnt - disc


    print(f"""Product name: {p_name}
    Units sold: {qty}
    price/unit: ${p_price}
    Total Amnt: ${amnt}
    Disc Rate: {d_rate * 100}%
    Discount: ${disc}
    Net Amount: ${n_amnt}
    """)

