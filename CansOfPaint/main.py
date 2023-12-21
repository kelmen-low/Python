import math
def paintCalc(height, width, cover):
    area = height * width
    fractionsOfCans = area / cover
    return math.ceil(fractionsOfCans)


print(paintCalc(3,9,5))