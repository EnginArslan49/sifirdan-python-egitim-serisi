
# while döngüsü, belirli bir koşul True olduğu sürece kod bloğunu tekrar eder.
# Koşul False olduğunda döngü durur. Bu nedenle koşulun bir noktada False olmasını sağlamak çok önemlidir (aksi halde sonsuz döngü oluşur).

#   YAPI:
#   while koşul:
#     yapılacak işlemler


# Örnek 1: Basit sayaç örneği
sayac = 0

while sayac < 5:        # koşul True olduğu sürece döner
    print("Sayaç değeri:", sayac)
    sayac += 1          # sayaç artırılarak döngü bir noktada sona erer

# Çıktı:
#   Sayaç değeri: 0
#   Sayaç değeri: 1
#   Sayaç değeri: 2
#   Sayaç değeri: 3
#   Sayaç değeri: 4


# Örnek 2: Kullanıcıdan veri alma
# Kullanıcı "çık" yazana kadar giriş ister.
giris = ""

while giris != "çık":
    giris = input("Bir şey yaz (çıkmak için 'çık' yaz): ")
    print("Yazdığın:", giris)


# NOT: while döngüsü koşula bağlı çalışır.
# - Eğer koşul hiçbir zaman False olmazsa döngü sonsuza kadar sürer.
# - Bu yüzden sayaç artırmak veya koşulu değiştiren bir işlem yapmak gerekir.
