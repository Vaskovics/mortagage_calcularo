
loan = float(input('Please enter amount of you mortgage: '))
period = int(input('Please enter perion in years: '))
interest = float(input('What is your interest Rate?: '))

period = period * 12
# loan = 286000
# period = 420
# interest = 2.05
interest = float(interest)/100/12

monthly_payments = loan * (interest * (1 + interest) ** period) / ((1 + interest) ** period - 1)

sum_mont_percent = 0
principal = 0
balance = loan
nb = 0

for p in range(period):
    sum_mont_percent = balance * interest
    principal = monthly_payments - sum_mont_percent
    balance = balance - principal
    nb += 1
    print(f"{nb} PaymentЖ {monthly_payments:.2f}£ interest: {sum_mont_percent:.2f}£ principal: {principal:.2f}£ balance: {balance:.2f}£  ")