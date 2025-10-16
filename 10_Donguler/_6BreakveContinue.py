
# Döngülerin akışını kontrol etmek için break ve continue komutları kullanılır.
#  break    → döngüyü tamamen durdurur.
#  continue → o adımdaki işlemi atlar, döngünün sonraki adımına geçer.


# Örnek 1: break kullanımı
for i in range(1, 10):  # 1'den başla 10'a kadar (10 dahil değil) git
    if i == 5:
        break  # i = 5 olduğunda döngü tamamen biter
    print("Sayı:", i)

# Çıktı:
# Sayı: 1
# Sayı: 2
# Sayı: 3
# Sayı: 4
# (i = 5 olunca döngü biter) Sayı: 5 YAZMAZ!


# Örnek 2: continue kullanımı
for i in range(1, 6):  # 1'den başla 6'ya kadar (6 dahil değil) git
    if i == 3:
        continue  # i = 3 olduğunda bu adımı atla, sonraki adıma geç
    print("Sayı:", i)

# Çıktı:
# Sayı: 1
# Sayı: 2
# (3 atlandı çünkü continue çalıştı)
# Sayı: 4
# Sayı: 5


# Örnek 3: while döngüsünde break
sayac = 0
while True:  # sonsuz döngü
    sayac += 1
    if sayac == 4:
        break  # döngüyü sonlandır
    print("Sayaç:", sayac)

# Yukardaki kodun mantığı aslında 1'den başla 4'e kadar (4 dahil değil) yazdır anlamı taşımaktadır. Kısaca: ( for sayi in range (1, 4) )

# Çıktı:
# Sayaç: 1
# Sayaç: 2
# Sayaç: 3
