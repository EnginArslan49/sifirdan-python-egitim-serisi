# Python'da değişken tanımlarken uyulması gereken kurallar:

# 1. Harf veya alt çizgi (_) ile başlamalı, rakamla başlayamaz:
sayi1 = 10       # Geçerli
# 1sayi = 10     # Geçersiz, rakamla başlayamaz

# 2. Büyük/küçük harf duyarlıdır:
isim = "Ali"
Isim = "Ayşe"
# Bu iki değişken farklıdır

# 3. Boşluk kullanılamaz, kelimeleri ayırmak için alt çizgi kullanılabilir:
ogrenci_sayisi = 30   # Geçerli
# ogrenci sayisi = 30 # Geçersiz, boşluk var

# 4. Özel karakterler kullanılamaz (harf, rakam ve _ dışında):
# isim$ = "Ahmet"   # Geçersiz
# yaş# = 20         # Geçersiz

# 5. Anahtar kelimeler değişken adı olamaz:
# if = 5            # Geçersiz, 'if' Python anahtar kelimesidir

# 6. Değişken ismi anlamlı olmalı, neyi temsil ettiğini anlatmalı:
s = 10              # Anlam belirsiz
yas = 10            # Daha açıklayıcı

# 7. Değişken isimlerinde Türkçe karakter (ç, ı, ö, ü, ş, ğ) kullanılmaması tavsiye edilir.

# Kötü kullanım (Türkçe karakterli)
yaş = 25
şehir = "İstanbul"

# İyi kullanım (Türkçe karakter kullanılmıyor)
yas = 25
sehir = "Istanbul"

# Özet:
# - Harf veya _ ile başla
# - Boşluk ve özel karakter kullanma (&, % gibi..)
# - Anahtar kelime kullanma (if, elif, else, for gibi..)
# - Anlamlı isimler seç
# Türkçe karakter (ç, ı, ö, ü, ş, ğ) kullanma
