
# Koşullu durumlar, belirli bir şartın doğru (True) veya yanlış (False) olmasına göre farklı kodların çalışmasını sağlar.
# Programın “karar verme” mekanizmasıdır.

#   YAPI:
#   if koşul:
#     koşul doğruysa çalışacak kod
#   elif başka_koşul:
#     ilk koşul yanlışsa, bu koşul doğruysa çalışır
#   else:
#     yukarıdaki hiçbir koşul doğru değilse çalışır

# Örnek:
sayi = 10

if sayi > 0:
    print("Sayı pozitif")        # Bu satır çalışır çünkü koşul True
elif sayi < 0:
    print("Sayı negatif")
else:
    print("Sayı sıfır")

# --------------------------
# Birden fazla koşul birleştirilebilir:
yas = 20
if yas >= 18 and yas <= 30:
    print("Genç yetişkin")       # True, bu aralıkta olduğu için çalışır
else:
    print("Farklı yaş aralığı")

# --------------------------
# NOT: Python'da girintiler (indentation) çok önemlidir!
# Koşula bağlı kodlar, if/elif/else satırının altına bir TAB veya 4 boşluk girilerek yazılmalıdır.