range = range(1,101)

for number in range:
    if (number % 5 == 0) & (number % 3 == 0):
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)