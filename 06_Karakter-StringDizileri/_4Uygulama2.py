
"""
    Klavyeden girilien öğrenci bilgisine göre örnek verilen çıktıyı veren programı yazınız.
    Örnek: Ahmet Yılmaz isimli öğrencinin 1. notu 60, 2. notu 60 ve 3. not ortalaması 60 olarak hesaplanmıştır.
"""

ad = input("Öğrencinin adını giriniz: ")
soyad = input("Öğrencinin soyadını giriniz: ")

not1 = input("Öğrencinin 1. notunu giriniz: ")
not2 = input("Öğrencinin 2. notunu giriniz: ")

ortalama = (float(not1) + float(not2)) / 2 # not ortalamasını hesapla

# Ekrana yazdırma
print(f"{ad} {soyad} isimli öğrencinin 1. notu {not1}, 2. notu {not2} ve not ortalaması {ortalama} olarak hesaplanmıştır.")
