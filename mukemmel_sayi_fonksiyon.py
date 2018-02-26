"""
Mukemmel sayı, tam bölenlerinin toplamı kendisi eden sayıdır.
"""

"""Proje başka bir yerde tamamlandığı için şimdilik yarım bırakılmıştır"""


mukemmeller = []
l = []
topla = 0

sayi = int(input("Sayı : "))

for i in range(1, sayi):
    if sayi % i == 0:
        l.append(i)

for k in l:
    topla = k + topla

if topla == sayi:
    mukemmeller.append(topla)
    print(mukemmeller)

