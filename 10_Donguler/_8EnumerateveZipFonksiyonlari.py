
# 1️⃣ enumerate() fonksiyonu
# enumerate(), bir liste veya dizideki elemanlara hem sıra numarası (index) hem de elemanın kendisini birlikte verir.
# Yani for döngüsünde hem index hem değerle aynı anda çalışmamızı sağlar.

#   YAPI:
#   for index, değer in enumerate(liste, başlangıç_indeksi):
#     işlemler...

# Örnek:
meyveler = ["elma", "armut", "muz"]

for sira, meyve in enumerate(meyveler, start=1):  # index 1’den başlar
    print(sira, "-", meyve)

# Çıktı:
# 1 - elma
# 2 - armut
# 3 - muz


# 2️⃣ zip() fonksiyonu
# zip(), birden fazla listeyi (veya diziyi) eleman bazında eşleştirir.
# Aynı sıradaki elemanları bir araya getirir ve tuple (demet) döndürür.

#   YAPI:
#   zip(liste1, liste2, ...)

# Örnek:
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [20, 25, 30]

for isim, yas in zip(isimler, yaslar):
    print(isim, "→", yas, "yaşında")

# Çıktı:
# Ali → 20 yaşında
# Ayşe → 25 yaşında
# Mehmet → 30 yaşında


# NOTLAR:
# - enumerate() → elemanların sıra numarasını verir.
# - zip() → iki veya daha fazla listeyi sırayla birleştirir.
# - zip() en kısa liste kadar eşleştirme yapar (fazla elemanlar dikkate alınmaz).
