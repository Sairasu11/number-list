number = int(input("Enter a number: "))

listnum = []

for data in range(number):
    number = int(input("my number: "))
    listnum.append(number)
    print(listnum)

for data in listnum:
    if data > 0:
        print(str(data) + "positive")
    elif data < 0:
        print(str(data) + "negative")