
# Uygulama 1: Bir aracın yakıt tipine göre (Benzin, Dizel, LPG) belirtilen mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız
"""
    Benzin: 57.05
    Dizel:  58.67
    LPG:    22.83
"""

benzinFiyat = 57.05
dizelFiyat = 58.67
lpgFiyat = 22.83
toplamFiyat = 0     # Başlangıçta toplam tüketim masrafını 0 olarak tanımladık. Bu değişkenin değeri seçilen yakıt türüne göre değiştirilecektir

ortalamaYakitTuketimi = float(input("100 km'deki ortalama yakıt tüketim miktarınız nedir? : "))
gidilenYol = float(input("Gittiğiniz toplam mesafe (KM): "))
yakitTipi = input("Yakıt tipiniz (Benzin, Dizel, LPG)? : ")

toplamYakitTuketimi = gidilenYol * (ortalamaYakitTuketimi / 100)    # Toplam gidilen yola göre yakıt tüketimini hesaplama

if yakitTipi == "Benzin":
    toplamFiyat = toplamYakitTuketimi * benzinFiyat
    print(f"Gittiğiniz {gidilenYol} KM yolda toplam {toplamFiyat} TL yakıt tüketiminiz olmuştur")

elif yakitTipi == "Dizel":
    toplamFiyat = toplamYakitTuketimi * dizelFiyat
    print(f"Gittiğiniz {gidilenYol} KM yolda toplam {toplamFiyat} TL yakıt tüketiminiz olmuştur")

elif yakitTipi == "LPG":
    toplamFiyat = toplamYakitTuketimi * lpgFiyat
    print(f"Gittiğiniz {gidilenYol} KM yolda toplam {toplamFiyat} TL yakıt tüketiminiz olmuştur")

else:
    print("Lütfen yakıt tipinizi doğru şekilde girdiğinizden emin olunuz")
