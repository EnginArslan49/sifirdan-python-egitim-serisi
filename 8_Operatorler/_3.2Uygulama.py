
a, b, c = 4, 8, (12, 2)
# Aşağıdaki soruları yukardaki kod satırına göre yapınız


# Uygulama 1: Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamının farkı nedir? (Alınan 1. sayı * Alınan 2. sayı) - (a + b+ c)
sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("1. Sayıyı Giriniz: "))

carpim = sayi1 * sayi2

sonuc = carpim - (a + b + c[0] + c[1])      # c[0] = 12 değerine, c[1] ise 2 değerine karşılık gelmektedir
# YÖNTEM 2 (Tek satırda): sonuc = (sayi1 * sayi2) - (a + b + c[0] + c[1])

print(f"Sonuç: {sonuc}")


# Uygulama 2: c'nin b'ye kalansız bölümünü hesaplayınız
kalansizBolum = (c[0] + c[1]) // b
print("Kalansız Bölüm:", kalansizBolum)


# Uygulama 3: a, b ve c sayılarının mod 7'si nedir?
cDegeri = c[0] + c[1]
modSonucu = (a + b + cDegeri) % 7
print("(a+b+c) % 7 Sonucu: ", modSonucu)


# Uygulama 4: b'nin a'ncı kuvettini (üssü) hesaplayınız
kuvvet = b ** a
print("b'nin a'ncı kuveti: ", kuvvet)