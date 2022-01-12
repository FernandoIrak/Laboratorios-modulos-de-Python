def isYearLeap(year):

    esBisiesto = False
    divisibleEntre_4 = year % 4
    divisibleEntre_100 = year % 100
    divisibleEntre_400 = year % 400

    if year >= 1582:
        if divisibleEntre_4 != 0:
            esBisiesto = False
        elif divisibleEntre_100 != 0:
            esBisiesto = True
        elif divisibleEntre_400 != 0:
            esBisiesto = False
        else:
            esBisiesto = True
    else:
        esBisiesto = False

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

def dayOfYear(year, month, day):
	dias = 0
	for mes in range(1, month):
		md = daysInMonth(year, mes)
		if md == None:
			return None
		dias += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return dias + day
	else:
		return None

print(dayOfYear(2000, 12, 31))