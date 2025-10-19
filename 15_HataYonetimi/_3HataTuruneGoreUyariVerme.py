
"""
    try-except yapısı ile hataları yakalayabilir ve türüne göre farklı işlemler yapabiliriz.

    - try bloğu: Hata oluşabilecek kodu içerir
    - except bloğu: Belirli hata türlerini yakalar ve uygun işlem yapılır
    - else bloğu: Hata oluşmazsa çalışır
    - finally bloğu: Her durumda çalışır
"""

# Örnek:
try:
    sayi = int(input("Bir sayı girin: "))  # ValueError olabilir
    print(10 / sayi)                        # ZeroDivisionError olabilir
except ValueError:
    print("Hata: Lütfen geçerli bir sayı girin.")   # Kullanıcı harf girerse ValueError yakalanır
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz.")          # Kullanıcı 2. sayıyı sıfır girerse ZeroDivisionError yakalanır
else:
    print("İşlem başarıyla tamamlandı.")            # Hata yoksa else çalışır
finally:
    print("Program sonlandı.")                      # finally her durumda çalışır (temizlik, log vb.)
