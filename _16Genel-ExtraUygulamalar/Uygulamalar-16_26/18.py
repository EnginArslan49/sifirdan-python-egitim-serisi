
"""
    Kullanıcıdan bir metin alınız ve metindeki kelime sayısını hesaplayarak ekrana yazdırınız.
    Girilen değer boş ise kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

while True:
    alinanMetin = input("Kelime sayısını hesaplayacağınız metni giriniz: ")

    if alinanMetin == "" or alinanMetin == " ":
        print("Lütfen bir metin giriniz!")

    else:
        bosluklardanAyrilmis = alinanMetin.split(" ")  # Alınan metni boşluklardan ayırma
        kelimeSayisi = len(bosluklardanAyrilmis)

        print(f"Girilen metnin kelime sayısı: {kelimeSayisi}\nGirilen Metin: {alinanMetin}")

        break
