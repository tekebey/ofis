
"""Belirtilen başlangıç, bitiş ve adım değerine göre, aralıktaki sayıların toplamı hesaplayan program"""

baslangic_sayisi = int(input("Başlangıç Sayısı : "))
bitis_sayisi = int(input("Bitiş Sayısı : "))
artis_miktari = int(input("Artış Miktarı : "))

x = 0
for i in range(baslangic_sayisi,bitis_sayisi + 1,artis_miktari):
    x = i + x

print("Başlangıç {} Bitiş {} Artış {} Toplamları {} ".format(baslangic_sayisi, bitis_sayisi, artis_miktari, x))

