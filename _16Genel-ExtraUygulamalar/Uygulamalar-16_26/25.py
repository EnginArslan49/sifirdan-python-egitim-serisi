
"""
    Kullanıcıdan bir sayı alınız ve bu sayının karekökünü hesaplayınız.
        Karekök hesaplama formülü: sayı ** 0.5
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

def karekokHesapla(deger):
    sonuc = 0

    try:
        deger = int(deger)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        sonuc = deger ** 0.5

    except ValueError:
        raise ValueError(f"Lütfen sayısal değer giriniz!")

    return f"Girilen {deger} sayısının karekökü: {sonuc}"



while True:
    try:
        sayi = input("Bir sayı giriniz: ")

        print(karekokHesapla(sayi))

        break

    except ValueError as hata:
        print(f"Hata: {hata}")
