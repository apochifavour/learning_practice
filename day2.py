user_name = "Alex"
user_age = 25
wallet_balance = 45.50
is_member = True

print(f"wallet_balance type: {type(wallet_balance)}")
rounded_balance = int(wallet_balance)

age_text = "Age: " + str(user_age)
print(age_text)

math_result = (5 + 3) * 2 ** 3 / 4
print(f"Math result: {math_result}")

items_bought = 45 // 10
price_per_item = round(45.50 / 3, 2)
print(f"Member: {is_member} | Items: {items_bought} | cost: ${price_per_item}") 