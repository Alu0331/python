m = {"January": 31,
          "February": 28,
          "March": 31,
          "April": 30,
          "May": 31,
          "June": 30,
          "July": 31,
          "August": 31,
          "September": 30,
          "October": 31,
          "November": 30,
          "December": 31}
d = 0
count = 0
def leap(year):
    l = True
    if year % 4 != 0:
        l = False
    elif year % 100 != 0:
        l = True
    elif year % 400 != 0:
        l = False
    return l
for year in range(1901,2001):
    l = leap(year)
    for i in m:
        d += m[i]
        if leap == True and m == "February":
            d += 1
        if d%7 == 0:
            count += 1
print(count)