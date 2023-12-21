studentHeights = [180,124,165,173,189,169,146]
total = 0
count = 0

for height in studentHeights:
    total += height
    count += 1

average = total / count
print(average)