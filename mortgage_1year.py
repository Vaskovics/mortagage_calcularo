amount = int(input("Please enter the amout of mortgage: "))
percentage = int(input("Please enter interest rate: "))
period = int(input("Please enter period of mortgage: "))

month = period * 12

month_body = amount/month


mouth_interest = 0
balance = amount

for i in range(month -1 ):
    balance -= month_body
    interest = (balance * (percentage/100)) / 12
    mouth_interest += round(interest, 2)

print("*"* 40)


mouth_interest_payment = mouth_interest / 11
suma1 = month_body + mouth_interest_payment
suma = round(suma1, 2)
print(f"You month payment is {suma}£")