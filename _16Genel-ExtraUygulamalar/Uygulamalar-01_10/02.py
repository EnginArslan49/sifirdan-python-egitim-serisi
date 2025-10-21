
"""
    Kullanıcıdan iki sayı alınız ve bu sayıların toplamını ekrana yazdırınız.
    Girilen değerler sayısal değilse kullanıcıyı uyarınız ve tekrar sayı girmesini sağlayınız.
"""

while True:
    sayi1 = input("1. Sayıyı Giriniz: ")
    sayi2 = input("2. Sayıyı Giriniz: ")

    try:
        sayi1 = int(sayi1)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır
        sayi2 = int(sayi2)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        sonuc = sayi1 + sayi2

        break

    except ValueError as hata:
        print(f"Lütfen doğru sayısal değerler girdiğinizden emin olunuz!\nHata: {hata}")


print(f"{sayi1} + {sayi2} = {sonuc}")
