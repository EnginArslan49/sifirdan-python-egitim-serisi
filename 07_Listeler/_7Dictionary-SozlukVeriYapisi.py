
# Dictionary (sözlük), verileri anahtar (key) ve değer (value) şeklinde tutar.
# {} süslü parantezler ile tanımlanır.
# Her key benzersiz olmalıdır.

# 1. Sözlük tanımlama
ogrenci = {
    "ad": "Zülal",
    "yas": 25,
    "bolum": "Bilgisayar Mühendisliği"
}

# 2. Sözlüğü ekrana yazdırma
print(ogrenci)

# 3. Belirli bir değere erişim (key kullanılır)
print(ogrenci["ad"])      # "Zülal"
print(ogrenci["yas"])     # 25

# 4. get() ile erişim (hata riskine karşı güvenli yöntem)
print(ogrenci.get("bolum"))        # "Bilgisayar Mühendisliği"
print(ogrenci.get("okul", "Yok"))  # "okul" yoksa varsayılan "Yok" döner

# 5. Yeni eleman ekleme
ogrenci["okul"] = "İTÜ"
print(ogrenci)

# 6. Mevcut değeri güncelleme
ogrenci["yas"] = 26
print("Güncellenmiş yaş:", ogrenci["yas"])  # 26

# 7. Eleman silme
ogrenci.pop("bolum")  # "bolum" anahtarını siler
print("Bölüm silindi:", ogrenci)

# 8. Tüm anahtarları (keys) listeleme
print("Anahtarlar:", ogrenci.keys())

# 9. Tüm değerleri (values) listeleme
print("Değerler:", ogrenci.values())

# 10. Anahtar-değer çiftlerini (items) birlikte alma
print("Anahtar-Değer çiftleri:", ogrenci.items())

# 11. Tüm sözlüğü temizleme
ogrenci.clear()
print("Sözlük temizlendi:", ogrenci)
