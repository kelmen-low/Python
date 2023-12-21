def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


inputYear = int(input("Please provide a year: "))

if isLeapYear(inputYear):
    print("Leap Year")
else:
    print("Not Leap Year")