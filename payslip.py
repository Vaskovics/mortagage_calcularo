suma = 0
while True:

    hours = float(input("Please eneter amount of hours or '0' to exit: "))
    if hours == 0:
        break
    rate = float(input("Plese eneter the rate: "))
    suma = suma + (hours * rate)


print(f"Your gross income is {suma:.2f}")

non_tax = 239.91
non_nin = 183.08
nin = (suma - non_nin) * 0.12
tax = (suma - non_tax) * 0.2
income = suma - nin - tax
print(f"Your net income is {income:.2f}, tax is {tax:.2f} and NIN is {nin:.2f}")
