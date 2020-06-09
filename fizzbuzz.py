print("Welcome to FizzBuzz")

number = int(input("Please select a number between 1 and 100: "))

for x in range(1, number+1):
    if x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    else:
        print(x)
