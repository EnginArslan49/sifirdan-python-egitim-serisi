
# ==============================
# PYTHON DICTIONARY (SÖZLÜK) METOTLARI
# ==============================

# Örnek sözlük tanımı
araba = {
    "marka": "Toyota",
    "model": "Corolla",
    "yil": 2020
}

# 1. copy() → Sözlüğün bir kopyasını çıkarır
kopya_araba = araba.copy()
print("Kopyalanan sözlük:", kopya_araba)

# 2. get() → Belirtilen key'e ait değeri döndürür
print("Model bilgisi:", araba.get("model"))        # "Corolla"
print("Renk bilgisi:", araba.get("renk", "Yok"))   # "Yok" (varsayılan değer)

# 3. items() → Tüm key-value çiftlerini döndürür
print("Anahtar-Değer çiftleri:", araba.items())

# 4. keys() → Anahtarları döndürür
print("Anahtarlar:", araba.keys())

# 5. values() → Değerleri döndürür
print("Değerler:", araba.values())

# 6. pop() → Belirtilen anahtardaki değeri siler
araba.pop("model")
print("Model silindikten sonra:", araba)

# 7. popitem() → Eklenen son key-value çiftini siler
araba.popitem()
print("Son eleman silindikten sonra:", araba)

# 8. update() → Sözlüğü güncellemek veya yeni değer eklemek için kullanılır
araba.update({"renk": "Kırmızı", "yil": 2021})
print("Güncellenmiş sözlük:", araba)

# 9. clear() → Sözlükteki tüm elemanları siler
araba.clear()
print("Tüm elemanlar silindi:", araba)  # {}
