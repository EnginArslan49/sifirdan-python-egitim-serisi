
# Birden fazla koşulu sırayla kontrol etmek için kullanılır.
# Python koşulları yukarıdan aşağıya kontrol eder.
# İlk True olan koşulun kodu çalışır, diğerleri atlanır.

# Yapı:
#   if koşul1:
#     koşul1 doğruysa bu blok çalışır
#   elif koşul2:
#     koşul1 yanlış ama koşul2 doğruysa bu blok çalışır
    # elif koşul3:
#     önceki koşullar yanlışsa ve bu koşul doğruysa çalışır
#   else:
#     hiçbir koşul doğru değilse çalışır


# Örnek:
sayi = 0

if sayi > 0:
    print("Sayı pozitif")
elif sayi < 0:
    print("Sayı negatif")
else:
    print("Sayı sıfır")     # sayi değişkenin değeri 0 olduğundan bu satır çalışacak


# Örnek 2: Not değerlendirme
not_ort = 85

if not_ort >= 90:
    print("Derece: A")
elif not_ort >= 80:
    print("Derece: B")      # not_ort  değişkenin değeri 80'den büyük ve 90'dan küçük olduğundan bu satır çalışacak
elif not_ort >= 70:
    print("Derece: C")
else:
    print("Derece: D")


# NOT: Yalnızca ilk doğru (True) koşulun bloğu çalışır.
"""
    Tüm koşullar False ise yalnızca else bloğu çalışır.
    elif bloklarının sayısı sınırsız olabilir.
"""