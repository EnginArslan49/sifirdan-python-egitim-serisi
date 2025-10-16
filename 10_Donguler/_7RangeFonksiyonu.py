
# range(), belirli bir sayı aralığı oluşturmak için kullanılır.
# Genellikle for döngülerinde sayısal tekrarları kontrol etmek için kullanılır.
# Üretilen değerler sıralı ve art arda sayılardır.

#   YAPI:
#   range(baslangic, bitis, adim)
#    baslangic → dahil edilir (varsayılan 0’dır)
#    bitis     → dahil edilmez (sona kadar gider ama bitiş sayısı hariçtir)
#    adim      → artış miktarı (varsayılan 1’dir)


# Örnek 1: Sadece bitiş değeri
for i in range(5):  # 0'dan başlar, 5 dahil değildir
    print(i)
# Çıktı: 0, 1, 2, 3, 4


# Örnek 2: Başlangıç ve bitiş değerleri
for i in range(2, 6):  # 2’den başlar, 6’ya kadar gider (6 hariç)
    print(i)
# Çıktı: 2, 3, 4, 5


# Örnek 3: Başlangıç, bitiş ve adım değeri
for i in range(0, 10, 2):  # 0'dan 10’a kadar 2’şer artırır
    print(i)
# Çıktı: 0, 2, 4, 6, 8


# Örnek 4: range() çıktısını listeye dönüştürme
sayilar = list(range(5))
print(sayilar)
# Çıktı: [0, 1, 2, 3, 4]
