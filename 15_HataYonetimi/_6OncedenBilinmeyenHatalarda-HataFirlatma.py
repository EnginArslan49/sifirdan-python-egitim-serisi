
"""
    Bazı durumlarda hangi tür hatanın oluşacağını önceden bilemeyiz. Bu gibi durumlarda tüm hata türlerini yakalamak için
`Exception` sınıfı kullanılır.

    Exception, tüm hata türlerinin (ValueError, TypeError, ZeroDivisionError vb.) temel sınıfıdır. Yani genel bir hata yakalayıcısıdır.

    Amaç:
     - Beklenmeyen tüm hataları tek bir yerde kontrol etmek
     - Programın çökmesini önlemek
"""

# Örnek:
try:
    sayi = int(input("Bir sayı girin: "))   # ValueError olabilir
    sonuc = 10 / sayi                       # ZeroDivisionError olabilir
    print("Sonuç:", sonuc)
except Exception as hata:
    # Tüm hata türlerini yakalar
    print("Bir hata oluştu:", hata)
finally:
    print("Program sonlandı.")

"""
    Özet:
     - except Exception: Bilinmeyen veya farklı türdeki tüm hataları yakalar.
     - hata değişkeni (as hata): Hatanın ayrıntılı mesajını tutar.
     - Dikkat: Geliştirme aşamasında faydalıdır ama üretim kodunda spesifik hata türlerini ayrı ayrı ele almak daha güvenlidir.
"""
