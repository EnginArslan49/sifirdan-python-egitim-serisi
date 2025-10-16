
# Uygulama 1: Klavyeden girilen 2 sayıdan hangisi büyüktür?
sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))

buyukluk = sayi1 > sayi2
print(f"{sayi1}, {sayi2}'den büyük mü? : " + str(buyukluk))


# Uygulama 2: Klavyeden girilen bir sayının tek / çift olma durumunu kontrol ediniz
girilenSayi = int(input("Bir Sayıyı Giriniz: "))

tekCiftDurumu = (girilenSayi % 2 == 0)
print(f"Girilen sayı çift mi? : {tekCiftDurumu}")


# Uygulama 3: Bir öğrencinin klavyeden girilen 3 notuna göre başarı durumunu kontrol ediniz. Ortalaması 50 ve üstü olanlar başarılı
not1 = float(input("1. Notunuz? : "))
not2 = float(input("2. Notunuz? : "))
not3 = float(input("3. Notunuz? : "))

ortalama = (not1 + not2 + not3) / 3
basariDurumu = ortalama >= 50

print(f"Öğrenci {round(ortalama, 2)} ortalama ile başarılı mı? : {basariDurumu}")       # round(ortalama, 2) ile ortalamanın virgülden sonrası 2 basamak haline getirildi