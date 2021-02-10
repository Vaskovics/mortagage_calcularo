loan = float(input('VICTOR and SANDOR please enter the price of the loan: '))
numPaym = float(input('Please enter how many monthly payments you will have: '))
interest = input('What is your interest Rate?: ')
interest = float(interest)/100/12
monthly_payments = loan * (interest * (1 + interest) ** numPaym) / ((1 + interest) ** numPaym - 1)
print(f"{round(monthly_payments, 2)}£")
