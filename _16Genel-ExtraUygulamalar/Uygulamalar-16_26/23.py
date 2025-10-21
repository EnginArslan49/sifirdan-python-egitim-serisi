
"""
    Kullanıcıdan bir sayı alınız ve bu sayıya kadar olan asal sayıları bir listeye ekleyip ekrana yazdırınız.
        Asal sayı => yalnızca 1 ve kendisine bölünebilen pozitif tam sayıdır.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

while True:
    try:
        sayi = input("Bir sayı giriniz: ")

        sayi = int(sayi)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        bolunebilenSayilar = 0
        for deger in range(2, sayi):
            if sayi % deger == 0:
                bolunebilenSayilar += 1

        if sayi == 1:
            print(f"Girilen {sayi} sayısı asal sayı değildir!")

        elif bolunebilenSayilar > 0:
            print(f"Girilen {sayi} sayısı asal sayı değildir!")

        else:
            print(f"Girilen {sayi} sayısı asal sayıdır")


        break

    except ValueError as hata:
        print(f"Lütfen sayısal değer giriniz!\nHata: {hata}")
