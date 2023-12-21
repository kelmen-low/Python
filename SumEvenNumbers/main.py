target = int(input("Target Number: "))

sum = 0
range = range(target + 1)

for number in range:
    if number % 2 == 0:
        sum += number
    else:
        continue

print(sum)