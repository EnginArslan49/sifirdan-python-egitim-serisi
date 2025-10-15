
# for döngüsü, bir koleksiyon (liste, dizi, string, tuple, vb.) veya sayı aralığı üzerinde sırayla gezinmek için kullanılır.
# Her yinelemede (tekrarda) eleman bir değişkene atanır.

#   YAPI:
#   for değişken in koleksiyon:
#     yapılacak işlemler


# Örnek 1: Liste üzerinde gezinme
meyveler = ["elma", "armut", "muz"]

for meyve in meyveler:
    print("Meyve:", meyve)
# Çıktı:
# Meyve: elma
# Meyve: armut
# Meyve: muz


# Örnek 2: range() fonksiyonu ile sayılar üzerinde döngü
for i in range(5):  # 0,1,2,3,4 üretir
    print("Sayı:", i)


# Örnek 3: range(başlangıç, bitiş, adım)
for i in range(2, 10, 2):  # 2’den 10’a kadar 2’şer artırır
    print("Çift sayı:", i)
# Çıktı: 2, 4, 6, 8


# Örnek 4: String üzerinde gezinme
kelime = "Python"
for harf in kelime:
    print("Harf:", harf)
"""
    Çıktı:
    Harf: P
    Harf: y
    Harf: t
    Harf: h
    Harf: o
    Harf: n
"""

# NOT:
# - for döngüsü, diziler ve koleksiyonlarda oldukça kullanışlıdır.
# - range() ile belirli bir aralıkta sayısal döngü oluşturulabilir.
# - Döngü, listedeki tüm elemanlar bitene kadar çalışır.
