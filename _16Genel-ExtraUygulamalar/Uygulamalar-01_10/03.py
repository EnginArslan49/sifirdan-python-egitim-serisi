
"""
    Kullanıcıdan bir sayı alınız ve bu sayının pozitif, negatif veya sıfır olduğunu ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar sayı girmesini sağlayınız.
"""

while True:
    sayi = input("Bir sayı Giriniz: ")

    try:
        sayi = int(sayi)    # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        if sayi == 0:
            print("Girilen Sayı 0'dır")
        elif sayi < 0:
            print("Girilen Sayı Negatiftir!")
        elif sayi > 0:
            print("Girilen Sayı Pozitiftir!")

        break
    except ValueError as hata:
        print(f"Lütfen doğru sayısal değerler girdiğinizden emin olunuz!\nHata: {hata}")
