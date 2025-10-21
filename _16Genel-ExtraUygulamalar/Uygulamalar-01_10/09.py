
"""
    Kullanıcıdan bir sayı alınız ve bu sayının faktöriyelini hesaplayarak ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

def faktoryelHesapla(deger):
    sonuc = 1
    try:
        deger = int(deger)
        for i in range(1, deger+1): # son değer dahil olmadığı için: deger+1
            sonuc *= i
    except ValueError:
        raise ValueError("Lütfen faktöryeli hesaplanacak sayıyı sayısal biçimde doğru girdiğinizden emin olup tekrar deneyiniz!")

    return f"{deger} sayısının faktöryeli: {sonuc}"



while True:
    try:
        sayi = input("Faktöriyeli hesaplanacak sayıyı giriniz: ")

        print(faktoryelHesapla(sayi))
        break
    except Exception as hata:
        print(f"Hata: {hata}")
