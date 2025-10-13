
"""
    Aşağıdaki verileri ogrenciler adlı liste içerisinde saklayınız
    Öğrenci 1: Yiğit Bilgi 2012 [70,85,90]
    Öğrenci 2: Hüsna Kurnaz 2015 [60,80,75]
    Öğrenci 3: Zekeriya Bilgi 2001 [55,85,70]
"""

ogrenci1 = ["Yiğit", "Bilgi", 2012, 70, 85, 90]
ogrenci2 = ["Hüsna", "Kurnaz", 2015, 60, 80, 75]
ogrenci3 = ["Zekeriya", "Bilgi", 2001, 55, 85, 70]

# Uygulama 2: Öğrencilerin yaşlarının toplamını hesaplayınız
bugunkuYil = 2025

yigitYas = bugunkuYil - ogrenci1[2]
husnaYas = bugunkuYil - ogrenci2[2]
zekeriyaYas = bugunkuYil - ogrenci3[2]

yasToplam = yigitYas + husnaYas + zekeriyaYas
print(f"Öğrencilerin Yaşlarının Toplamı: {yasToplam}")


# Uygulama 3: Öğrencilerin not ortalamalarını hesaplayınız
yigitNotlar = ogrenci1[3] + ogrenci1[4] + ogrenci1[5]
husnaNotlar = ogrenci2[3] + ogrenci2[4] + ogrenci2[5]
zekeriyaNotlar = ogrenci3[3] + ogrenci3[4] + ogrenci3[5]

print(f"Yiğit adlı öğrencinin not ortalaması: {yigitNotlar / 3}")
print(f"Hüsna adlı öğrencinin not ortalaması: {husnaNotlar / 3}")
print(f"Zekeriya adlı öğrencinin not ortalaması: {zekeriyaNotlar / 3}")

print(f"Tüm öğrencilerin not ortalaması: { (yigitNotlar + husnaNotlar + zekeriyaNotlar) / 9 }")