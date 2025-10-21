
"""
    Kullanıcıdan bir sayı alınız ve bu sayıya kadar olan Fibonacci sayılarını ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.

    - Fibonacci sayıları, her sayının kendisinden önceki iki sayının toplamı olduğu bir sayı dizisidir.
    Dizinin başlangıcı genellikle 0 ve 1 olarak alınır: 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

def fibonnaciSayilariYaz(deger):

    fibonacciListesi = [0, 1]
    ucuncuDeger = 0

    try:
        deger = int(deger)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu (ValueError) çalışır

        for i in range(1, deger-1): # Fibonacci listesinde ilk 2 değer verildiği için son değeri almaz bizde 1 adet daha alma (-1) diyerek girilen sayı ne ise -2 kadar gitmesini sağladık
            ucuncuDeger = fibonacciListesi[len(fibonacciListesi) - 1] + fibonacciListesi[len(fibonacciListesi) - 2]
            fibonacciListesi.append(ucuncuDeger)

    except ValueError:
        raise ValueError("Lütfen girdiğiniz değeri sayısal biçimde yazıp tekrar deneyiniz!")

    return print(fibonacciListesi)



while True:
    sayi = input("Bir sayı giriniz: ")

    try:
        print(fibonnaciSayilariYaz(sayi))
        break

    except ValueError as hata:
        print(f"Hata: {hata}")
