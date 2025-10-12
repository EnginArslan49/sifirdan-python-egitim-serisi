
"""
    UYGULAMA 1: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız
    km'yi mil'e çevirme formülü: km / 1.609344
"""

# ÇÖZÜM

km= float(input("Mil'e Çevrilecek KM'yi Giriniz: ")) # Kullanıcının km'yi 10.5 gibi ondalıklı sayı girmesine karşın float veri tipine çevirdik

mil = km / 1.609344

# Ekrana Yazdırma
print("Girilen KM: " + str(km))
print(str(km) + " Km toplam " + str(mil) + " eder")
