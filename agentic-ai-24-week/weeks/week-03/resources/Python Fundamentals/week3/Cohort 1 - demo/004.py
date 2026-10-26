# Find the total amount of sale based on the following discount policy
# if the total gross sale is > $2000, then give a discount of 7.5%
# if the total gross sale is > $1500 - $2000, then give a discount of 5%
# if the total gross sale is > $1000 - $1500, then give a discount of 2.5%
# Input the per unit cost, qty, and product name from the user.
# do this for 2 products

no = int(input("How many products: "))

for i in range(0, no): # for loop - for values in range 0, 1, 2, no-1, do this
    p_name = input(f"Product name {i+1}: ")
    price = float(input("Per unit price: "))
    qty = int(input("Units sold: "))

    t_g_sales = price * qty  # total gross sales
    d_rate = 0
    t_n_sales = t_g_sales   # total net sales

    """
    t_g_sales > 2000
    ---> d_rate = 0.075
    ---> t_n_sales = t_g_sales - (t_g_sales * d_rate)
    """
    if (t_g_sales > 2000):
        d_rate = 0.075
    elif (t_g_sales <= 2000 and t_g_sales > 1500):
        d_rate = 0.05
    elif (t_g_sales <= 1500 and t_g_sales > 1000):
        d_rate = 0.025

    t_n_sales = t_g_sales - ( t_g_sales * d_rate)

    print (f"""
    {qty} units of {p_name} Sold at ${price}.
    Gross Sales amount ${t_g_sales}.
    Discount offered at {d_rate*100}%.
    Total discount offered ${t_g_sales * d_rate}.
    Net sales amount ${t_n_sales}
    """)
