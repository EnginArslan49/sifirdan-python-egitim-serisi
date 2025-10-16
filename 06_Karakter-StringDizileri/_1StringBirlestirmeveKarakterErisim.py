

# Değişkenleri tanımlayalım
filmAdi = "Yapay Zeka"
filmTuru = "Bilim Kurgu"
filmSuresi = "2 Saat 15 Dakika"

# Değişkenleri birleştirip anlamlı bir metin oluşturuyoruz
bilgi = "Film adı: " + filmAdi + " | Türü: " + filmTuru + " | Süresi: " + filmSuresi

# Tüm metni ekrana yazdır
print(bilgi)

# String içinde karakterlere indeks ile erişim
# [0] → ilk karakteri verir
print(bilgi[0])   # İlk karakter

# [-1] → son karakteri verir
print(bilgi[-1])  # Son karakter

# [0:10] → 0. indexten 10. indexe kadar olan kısmı verir (10 dahil değil)
print(bilgi[0:10])  # Metnin ilk 10 karakteri

# [::2] → Baştan sona giderken her 2. karakteri alır
print(bilgi[::2])   # ÇIKTI: Fl d:YpyZk  üü ii ug  üei  at1 aia

# len() → metnin uzunluğunu verir
print("Metnin uzunluğu:", len(bilgi))
