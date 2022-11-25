# bekérsz egy tetszőleges számot
# kiírod a HUF "5ösre kerekített" berzióját

szam:int = int(input('írj be egy tetszőleges pozitív számot: '))
if szam % 5 <= 2:
    szam -= szam % 5
elif szam % 5 >= 3:
    szam += (5 - (szam % 5))

print(f'a HUF kerekítési szabályainak megfelelő érték: {szam}')

# print(5 * round(szam / 5))

# tesztekhez:
# 1992 -> 1990
# 2006 -> 2005
# 1705 -> 1705
#  999 -> 1000
#  768 ->  770
# 1333 -> 1335
# 1300 -> 1300