

# ==============================
# String dilimleme (slicing) örneği
# ==============================

kitap = "Veri Bilimi ile Python"

# len() → metnin uzunluğunu bulur
uzunluk = len(kitap)
print("Metin uzunluğu:", uzunluk)  # 22 karakter

# Son karaktere erişim (uzunluk - 1)
print("Son karakter:", kitap[uzunluk - 1]) # Saymaya 0'dan başlandığı için -1 diye yazılmalı

# 0:4 → 0. indexten 4. indexe kadar (4 dahil değil)
print(kitap[0:4])    # "Veri"

# [:4] → baştan 4. indexe kadar (kısa yazım)
print(kitap[:4])     # "Veri"

# [5:11] → 5. indexten 11. indexe kadar (11 dahil değil)
print(kitap[5:11])   # "Bilimi"

# [12:] → 12. indexten sona kadar
print(kitap[12:])    # "ile Python"

# [-6:] → sondan 6 karakter
print(kitap[-6:])    # "Python"

# [::2] → Baştan sona her 2. karakteri alır
print(kitap[::2])    # Aralıklı karakterler

# [::-1] → Metni tersten yazdırır
print(kitap[::-1])   # "nohtyP eli imiliB ireV"
