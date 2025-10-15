
# Döngüler (loops), bir işlemi belirli bir sayıda veya bir koşul sağlandığı sürece tekrar tekrar çalıştırmak için kullanılır.
# Yani “tekrar eden işleri otomatikleştirmeyi” sağlar.

# Python'da iki temel döngü türü vardır:
# 1. for döngüsü → belirli bir sıradaki elemanlar üzerinde gezinir.
# 2. while döngüsü → koşul True olduğu sürece çalışır.

# Örnek 1: for döngüsü
for i in range(5):   # 0'dan 4'e kadar sayıları üretir
    print("Tekrar:", i)


# Örnek 2: while döngüsü
sayac = 0
while sayac < 3:      # koşul True olduğu sürece çalışır
    print("Sayaç:", sayac)
    sayac += 1        # koşulu değiştirmek için sayaç artırılır


# NOT:
# Döngülerde koşul doğru (True) kaldığı sürece tekrar yapılır.
# Sonsuz döngü riskine karşı koşulun bir noktada False olmasını sağlamalıyız.
