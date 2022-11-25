from random import randint

szamok:list[int] = []
for i in range(100):
    szam:int = randint(200, 1999) * 5
    szamok.append(szam)
    print(szamok[i], end=' ')
    if (i+1) % 10 == 0: print(end='\n')

eo:int = 0
for szam in szamok:
    eo += szam
print(f'lista elemeinek összege: {eo}')
print(f'elemek összege máképp:   {sum(szamok)}')

esz4K5K:int = 0
eo4K5K:int = 0
for szam in szamok:
    if 4000 <= szam < 5000:
        esz4K5K += 1
        eo4K5K += szam
print(f'[4K;5K) közti elemek átlaga: {eo4K5K / esz4K5K}')

maxi:int = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
print(f'a legnagyobb elem ({szamok[maxi]}) indexe a listában: {maxi}')
print(f'sor: {maxi // 10 + 1}, oszlop: {maxi % 10 + 1}')

eo25Kig:int = 0
i:int = 0
while eo25Kig < 25000:
    eo25Kig += szamok[i]
    i += 1
print(f'az első {i} elemet kell összeadni, hogy elérjem a 25K-t')

i:int = 0
while i < len(szamok) and szamok[i] % 65 != 0:
    i += 1
if i < len(szamok):
    print(f'van 65 többszöröse - érték: {szamok[i]}, index: {i}')
else: print(f'nincs a listában 65-el östható elem')

db3k:int = 0
for szam in szamok:
    if szam // 1000 == 3: db3k += 1
print(f'összesen {db3k} db olyan szám van, ami 3-assal kezdődik')

i:int = 0
while szamok[i] < 3500 or szamok[i] > 4500:
    i += 1
print(f'szerintem a {szamok[i]} már elfogadható órabér lenne (index: {i})')

kerek100asok:list[int] = []
for szam in szamok:
    if szam % 100 == 0:
        kerek100asok.append(szam)

for szam in kerek100asok:
    if szam // 1000 == szam % 1000 // 100:
        print(f'#{szam}#', end=' ')
    else: print(szam, end=' ')