
share_growth = float(input("Please enter the annual growth percentage: ")) #1.0877
property_growth = 1.044
share_growth = (share_growth / 100) + 1

deposit = float(input("Please enter the deposit: "))
capitalization = int(input("Please enter the sum of monthly capitalization: "))
period = int(input("Please enter period of investment: "))

period = period * 12
monthly_interest_rate = pow(share_growth, 1/12)

balance = deposit
capitalization_amount = deposit
for month in range(1, period):
    capitalization_amount += capitalization
    balance *= monthly_interest_rate
    print(f"{month: 4} month, balance is {balance + capitalization:.2f}£, amount of capitalization is {capitalization_amount}£")
    balance += capitalization