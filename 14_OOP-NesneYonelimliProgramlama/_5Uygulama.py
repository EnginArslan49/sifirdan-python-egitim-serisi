
"""
    ADIM 1: BankaHesabi isminde bir sınıf tanımlayınız
    ADIM 2: Üretilen her bir nesne "hesapSahibi" isminde bir özelliğe sahip olmalıdır. Ör: BankaHesabi("Engin Arslan")
    ADIM 3: Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır
    ADIM 4: Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışardan yatırılacak miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarını geriye döndürün
    ADIM 5: Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışardan çekilecek miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün
    ADIM 6: Üretilen her bir nesne için "bakiyeSorgula" metodu oluşturun ve kişinin bakiyesini geriye döndürün
"""


class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapinAitOlduguKisi = hesapSahibi
        self.bakiye = 0.0

    def paraYatir(self, verilenMiktar):
        if verilenMiktar > 0:
            self.bakiye += verilenMiktar
            print(f"{verilenMiktar}TL yatırma işleminiz başarıyla gerçekleştirilmiştir")
        return self.bakiye

    def paraCek(self, istenenMiktar):
        if (istenenMiktar > 0) and self.bakiye >= istenenMiktar:
            self.bakiye -= istenenMiktar
            print(f"{istenenMiktar}TL yatırma işleminiz başarıyla gerçekleştirilmiştir")

            return self.bakiye
        else:
            return print(f"Bakiyeniz Yetersiz!")

    def bakiyeSorgula(self):
        return self.bakiye



kisiAdi = input("Hesabın ait olduğu kişi? : ")

# Hesabın ait olduğu kişi alanı girilene kadar sürekli aynı soruyu sor
while kisiAdi == "":
    kisiAdi = input("Hesabın ait olduğu kişi? : ")

hesap = BankaHesabi(kisiAdi)    # hesap bilgisi adıyla BankaHesabi sınıfından örnek oluşturduk

while True:     # while True: ile sonsuz döngüye aldık sürekli işlemimizi sorması adına
    menuSecim = input("1- Para Yatır\n2- Para Çek\n3- Bakiye Sorgula\nSeçiminiz? : ")

    if menuSecim == "1":
        miktar = int(input("Yatırmak İstediğiniz Miktar: "))
        hesap.paraYatir(miktar)

    elif menuSecim == "2":
        miktar = int(input("Çekmek İstediğiniz Miktar: "))
        hesap.paraCek(miktar)

    elif menuSecim == "3":
        print(f"SN. {kisiAdi} bakiyeniz: {hesap.bakiyeSorgula()}")

    else:
        print("Lütfen menüden doğru menü elemanını seçiniz! ")
