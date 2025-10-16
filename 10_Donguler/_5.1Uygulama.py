
# Uygulama 1: Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız (while döngüsü ile)
baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))

toplam = 0          # Toplam değeri tutacak değişkene başlangıçta 0 değeri atandı

z = baslangic
while z <= bitis:
    if z % 2 == 0:
        toplam += z

    z += 1  # Sonsuz döngüye girmemesi için her döngüde z değeri 1 arttırılır

print(f"{baslangic} - {bitis} sayısı arasındaki çift sayıların toplamı: {toplam}")




# Uygulama 2: 1-100 arasındaki sayıları azalan şekilde (100, 99, 98..) şeklinde yazdırınız
baslangicDegeri = 100

while baslangicDegeri >= 1: # 100 sayısı 1'e eşit veya büyük olana kadar devam ettirme
    print(baslangicDegeri)
    baslangicDegeri -= 1    # Sonsuz döngüye girmemesi için her döngüde baslangicDegeri değişekni 1 azaltılır




# Uygulama 3: Kullanıcıdan aldığınız 5 sayıyı sıralı bir şekilde ekrana yazdırınız
sayiDegeri = 1

sayiListesi = []                # Sayıları sıralama için bir boş liste tanımlandı değerleri while döngüsü içinde tek tek kullanıcıdan alınıp atanacak

while sayiDegeri <= 5:
    sayi = int(input(f"{sayiDegeri}. sayıyı giriniz: "))

    sayiListesi.append(sayi)    # Kullanıcıdan alınan sayıyı listeye ekleme

    sayiDegeri += 1             # Sonsuz döngüye girmemesi için her döngüde sayiDegeri değişkeni 1 arttırılır

# Uygulama buraya gelince tüm değerler kullanıcıdan alınmış olup sıralama işlemine geçecektir
sayiListesi.sort()  # sayiListesi'ni küçükten büyüğe sıralama

# sayiListesi adındaki sıralanmış listeyi ekrana yazdırma
print(sayiListesi)




# Uygulama 4: Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece username girişi istesin
username = ""

# Kullanıcı hiçbirşey yazmazsa veya boşluk yazıp enter'a basarsa kullanıcıya sürekli Kullanıcı Adını soracak döngü
while username == " " or username == "":
    username = input("Kullanıcı Adınız: ")

print(f"BAŞARILI! Kullanıcı adınız en az 1 karakterden oluşuyor. {username}")
