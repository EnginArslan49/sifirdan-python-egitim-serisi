
# Uygulama 2: Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalamasını hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi hesaplayınız.
"""
    0 - 24 =>   0
    25 - 44 =>  1
    45 - 54 =>  2
    55 - 69 =>  3
    70 - 84 =>  4
    85 - 100 => 5
"""


yazili1 = float(input("1. Yazılı Notunuz: "))
yazili2 = float(input("2. Yazılı Notunuz: "))
sozlu = float(input("Sözlü Notunuz: "))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if (ortalama >= 0) and (ortalama <= 24):
    print(f"{ortalama} ile notunuz: 0")

elif (ortalama >= 25) and (ortalama <= 44):
    print(f"{ortalama} ile notunuz: 1")

elif (ortalama >= 45) and (ortalama <= 54):
    print(f"{ortalama} ile notunuz: 2")

elif (ortalama >= 55) and (ortalama <= 69):
    print(f"{ortalama} ile notunuz: 3")

elif (ortalama >= 70) and (ortalama <= 84):
    print(f"{ortalama} ile notunuz: 4")

elif (ortalama >= 85) and (ortalama <= 100):
    print(f"{ortalama} ile notunuz: 5")

else:
    print("Lütfen yazılı ve sözlü notlarınızı doğru girdiğinizden emin olunuz!")
