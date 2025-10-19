
"""
    1. ValueError: Geçersiz veri tipi girişi
       Örnek:
            int("abc")  # Hata: sayıya dönüştürülemez

    2. TypeError: Uygun olmayan veri tipiyle işlem yapma
       Örnek:
            "5" + 3     # Hata: string ve int toplanamaz

    3. NameError: Tanımlanmamış değişken kullanma
       Örnek:
            print(x)    # Hata: x tanımlı değil

    4. IndexError: Liste sınırları dışına erişim
       Örnek:
           liste = [1,2];
           print(liste[5])

    5. KeyError: Sözlükte olmayan anahtara erişim
       Örnek:
           sozluk = {"a":1};
           print(sozluk["b"])

    6. FileNotFoundError: Bulunmayan dosyayı açmaya çalışma
       Örnek:
           open("olmayan_dosya.txt")

    7. ZeroDivisionError: Bir sayıyı sıfıra bölme
        Örnek:
            10 / 0
"""
