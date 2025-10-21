
"""
    Kullanıcıdan bir sayı alınız ve bu sayıya kadar (kullanıcının girmiş olduğu sayı dahil) olan tek sayıların toplamını hesaplayarak ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

while True:
    try:
        alinanSayi = input("Bir sayı giriniz: ")

        alinanSayi = int(alinanSayi)    # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        toplam = 0

        for sayi in range(1, alinanSayi+1): # 1'den başla alınan sayıya kadar git. (Son sayı dahil olmadığı için alinanSayi+1 yazıldı)
            if sayi % 2 == 1:   # sayi % 2 işleminin sonucu 1 ise sayı tektir
                # TEK SAYI Bloğu
                toplam += sayi

        print(f"1-{alinanSayi} arasındaki TEK sayıların toplamı: {toplam}")

        break

    except ValueError as hata:
        print("Lütfen sayısal bir değer girdiğinizden emin olup tekrar deneyin!")
