
"""
    1’den 50’ye kadar olan çift sayıları bir listeye ekleyiniz ve bu listeyi ekrana yazdırınız.
"""

ciftSayilar = []    # Başta boş

for sayi in range(1,51): # son sayı dahil olmadığından 50+1
    if sayi % 2 == 0:    # sayi % 2 sonucu 0 gelirse sayı çifttir
        ciftSayilar.append(sayi)    # ciftSayilar listesine ekleme

print(ciftSayilar)
