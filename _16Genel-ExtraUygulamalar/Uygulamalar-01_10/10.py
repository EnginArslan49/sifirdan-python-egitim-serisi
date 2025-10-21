
"""
    Kullanıcıdan bir sayı alınız ve bu sayının asal olup olmadığını kontrol ederek sonucu ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

def asalSayiKontrolu(deger):
    asalMi = "Evet"

    try:
        deger = int(deger)

        for i in range(2, deger):
            if deger % i == 0:
                asalMi = "Hayır"

    except ValueError:
        raise ValueError("Lütfen asal sayı durumu kontrol edilecek sayıyı sayısal biçimde doğru girdiğinizden emin olup tekrar deneyiniz!")

    return asalMi



while True:

    sayi = input("Asal sayı durumu kontrol edilecek sayıyı giriniz: ")

    try:
        print(asalSayiKontrolu(sayi))

    except Exception as hata:
        print(f"Hata: {hata}")
