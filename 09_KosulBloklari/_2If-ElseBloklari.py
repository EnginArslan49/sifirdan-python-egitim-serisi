
# if-else yapısı, bir koşulun doğru (True) ya da yanlış (False) olmasına göre iki farklı kod bloğundan birini çalıştırır.

# Genel yapı:
#   if koşul:
#     koşul doğruysa bu blok çalışır
#   else:
#     koşul yanlışsa bu blok çalışır

# Örnek 1:
sayi = 5

if sayi > 0:
    print("Sayı pozitif")    # Bu satır çalışır çünkü koşul True
else:
    print("Sayı negatif veya sıfır")


# Örnek 2:
kullanici = "admin"

if kullanici == "admin":
    print("Giriş başarılı!")  # Koşul True → bu blok çalışır
else:
    print("Yetkisiz kullanıcı!")  # Koşul False → bu blok çalışmaz

# NOT: if-else yapısı tek bir koşulu kontrol eder.
"""
    Daha fazla durum kontrolü gerekiyorsa elif kullanılmalıdır.
"""