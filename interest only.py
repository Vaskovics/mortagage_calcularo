house_price = float(input("What is the prise for house?\n"))
deposit_percent = float(input("What is the deposit percentage required?\n"))
interest_rate = float(input("What is the interest rate?\n"))

deposit = house_price * (deposit_percent/100)

mounthly_payment = ((house_price - deposit)  * (interest_rate / 100)) / 12
print(f"Monthly payment is {mounthly_payment:.0f}£ and required deposit is {deposit:.0f}£")