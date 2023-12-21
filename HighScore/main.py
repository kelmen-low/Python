example = [13,25,76,47,89,23]
max = 0

for number in example:
    if number > max:
        max = number
    else:
        continue

print(max)