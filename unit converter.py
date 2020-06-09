print("Welcome to the unit converter. This is a possibility to convert your stated kilometers into miles!")
while True:
    user_input = input("Please state your number of kilometers you want to convert: ")
    km = int(user_input)


    print("Converted into miles: " +str(int(km * 0.62137)))
    more = str(input("Do you want to convert another number of km? Please enter Yes or No? "))
    if more == str("No"):
        print("Thank you for using the converter and have a good day")
        break
    else:
        print("Let's continue...")
