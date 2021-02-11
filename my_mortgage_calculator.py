name = input("Please enter you name: ")

while True:
    loan = input('Please enter amount of you mortgage: ')
    if loan.isdigit():
        break
while True:
    period = input('Please enter perion in month: ')
    if period.isdigit():
        break
while True:
    try:
        interest = (float(input('What is your interest Rate?: ')))
        break
    except ValueError:
        interest = (float(input('What is your interest Rate?: ')))


loan = float(loan)
period = int(period)
interest = float(interest)

interest = float(interest)/100/12

monthly_payments = loan * (interest * (1 + interest) ** period) / ((1 + interest) ** period - 1)
# print(monthly_payments)

sum_mont_percent = 0
principal = 0
balance = loan
nb = 0

sfix = 0

with open(f"{name}.txt", "w", encoding="utf-8") as documentation:
    for p in range(period):
        sum_mont_percent = balance * interest
        principal = monthly_payments - sum_mont_percent
        balance = balance - principal
        nb += 1
        sfix +=  sum_mont_percent
        print(f"{nb} monthly payment: {monthly_payments:.2f}£| interest: {sum_mont_percent:.2f}£| principal: {principal:.2f}£| "
              f"balance: {balance:.2f}£| sum of interest payed is: {sfix: .2f}£ ", file=documentation)
