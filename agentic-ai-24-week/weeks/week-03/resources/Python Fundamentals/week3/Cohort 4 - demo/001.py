p_name = input("product name? ")
p_price = float(input("price per unit ($)? "))
qty = int(input("units sold? "))
amnt = p_price * qty



# print(p_name, "sold", qty, "units at $", p_price, "for $", amnt)

# print(f"{p_name} sold {qty} units at ${p_price} for ${amnt}")  # f - formatted

multi_line = '''
This is a multi-
line text and
        will print as is.
    even the sapces
            and the tabs will print.
'''

print(multi_line)

'''
this multi line string is not assinged,
so it will be treated as a comment by Python
'''

print(f"""Product name: {p_name}
Units sold: {qty}
price/unit: ${p_price}
Total Amnt: ${amnt}""")

