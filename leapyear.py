def leapyear(year):
    isLeapYear = False
    if (year %4) == 0:
        if (year %100) ==0:
            isLeapYear = False
            if (year %400) == 0:
                isLeapYear = True
                return isLeapYear
            return isLeapYear
        isLeapYear =True
        return isLeapYear

year = int(input("Please secelt a year to check: "))
isLeapYear = leapyear(year)
print("The result of the test is: ",isLeapYear)