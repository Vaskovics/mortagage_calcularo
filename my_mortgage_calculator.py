name = input("Please enter you name: ")
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid number been entered, please try again: ")

loan = get_number("Please enter amount of you mortgage: ")
period = get_number("Please enter perion in month: ")
interest = get_number("What is your interest Rate: ")

loan = float(loan)
period = int(period)
interest = float(interest)

interest = float(interest)/100/12

monthly_payments = loan * (interest * (1 + interest) ** period) / ((1 + interest) ** period - 1)

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
