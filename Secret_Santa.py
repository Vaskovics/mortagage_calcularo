import random
import smtplib
list_names = ["Viktor", "Sveta", "George", "Viktoria", "Sandor", "Natka", "Maks", "Maria"]
left_names = list_names
result = {

}
switch = True
while switch:
    for name in list_names:
        choice = random.choice(left_names)
        result[name] = choice
        if name == choice:
            result.clear()

            break
    if len(list_names) == len(result):
        switch = False

for key, value in result.items():
    print(key, value)
print(len(result))

me_email = "v.vaskovics@gmail.com"
password = "Vitya2010"

contact = {
    "Viktor": "vasha2020@gmail.com",
    "Sveta": "sv.dobrunik@gmail.com",
    "Sandor": "sandor@gmail.com",
    "Natka": "natka@gmail.com",
    "George": "george@gmail.com",
    "Viktoria": "viktoria@gmail.com",
    "Maria": "maria@gmail.com",
    "Maks": "maks@gmail.com"
}

me_email = "v.vaskovics@gmail.com"
password = "Vitya2010"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(me_email, password)


for k, v in contact.items():
    receiver = v
    for key in contact.keys():
        for key, value in result.items():
            if k == key:
                message = value
    connection.sendmail(me_email, to_addrs=receiver, msg=message)



connection.close()