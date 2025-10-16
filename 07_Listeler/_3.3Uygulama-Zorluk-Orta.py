
"""
    Aşağıdaki verileri ogrenciler adlı TEK liste içerisinde saklayınız
        Yiğit Bilgi 2012 [70,85,90]
        Hüsna Kurnaz 2015 [60,80,75]
        Zekeriya Bilgi 2001 [55,85,70]
"""

ogrenciler = [ ["Yiğit", "Bilgi", 2012, 70, 85, 90], ["Hüsna", "Kurnaz", 2015, 60, 80, 75], ["Zekeriya", "Bilgi", 2001, 55, 85, 70] ]

# Uygulama 2: Öğrencilerin yaşlarının toplamını hesaplayınız
bugunkuYil = 2025

yigitYas = bugunkuYil - ogrenciler[0][2]
husnaYas = bugunkuYil - ogrenciler[1][2]
zekeriyaYas = bugunkuYil - ogrenciler[2][2]

yasToplam = yigitYas + husnaYas + zekeriyaYas
print(f"Öğrencilerin Yaşlarının Toplamı: {yasToplam}")


# Uygulama 3: Öğrencilerin not ortalamalarını hesaplayınız
yigitNotlar = ogrenciler[0][3] + ogrenciler[0][4] + ogrenciler[0][5]
husnaNotlar = ogrenciler[1][3] + ogrenciler[1][4] + ogrenciler[1][5]
zekeriyaNotlar = ogrenciler[2][3] + ogrenciler[2][4] + ogrenciler[2][5]

print(f"Yiğit adlı öğrencinin not ortalaması: {yigitNotlar / 3}")
print(f"Hüsna adlı öğrencinin not ortalaması: {husnaNotlar / 3}")
print(f"Zekeriya adlı öğrencinin not ortalaması: {zekeriyaNotlar / 3}")

print(f"Tüm öğrencilerin not ortalaması: { (yigitNotlar + husnaNotlar + zekeriyaNotlar) / 9 }")