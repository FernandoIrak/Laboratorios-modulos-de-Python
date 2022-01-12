def isYearLeap(year):
    esBisiesto = False
    divisibleEntre_4 = year % 4
    divisibleEntre_100 = year % 100
    divisibleEntre_400 = year % 400

    if divisibleEntre_4 != 0:
        esBisiesto = False
    elif divisibleEntre_100 != 0:
        esBisiesto = True
    elif divisibleEntre_400 != 0:
        esBisiesto = False
    else:
        esBisiesto = True

    return esBisiesto


def daysInMonth(year, month):
    diasEnMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    esBisiesto = isYearLeap(year)
    dias = 0

    if (year < 1582) or (month < 1 or month > 12):
        return None

    if esBisiesto and month == 2:
        dias = 29
    else:
        dias = diasEnMeses[month - 1]
    return dias


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")