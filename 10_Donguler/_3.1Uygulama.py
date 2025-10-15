
sayilar = [3, 5, 7, 9, 19, 174, 679]
# Aşağıdaki uygulamaları yukardaki sayilar listesine göre yapınız

# Uygulama 1: 'sayilar' listesindeki her bir elemanı for döngüsü ile yazdırın
for sayi in sayilar:    # sayilar listesinin uzunluğu kadar ilerler ve her eleman sayi değişkeni içerisine kopyalanır
    print(sayi)         # her döngüde sayi değişkenine kopyalanan değer ekrana yazdırılır



# Uygulama 2: 'sayilar' listesinde hangi sayılar 3'ün katıdır
for x in sayilar:
    if x % 3 == 0:   # her döngüde gelen değer mod 3'ün 0 olup olmadığına bakılır. (% 3 == 0) ise 3'ün katıdır
        print(f"{x} sayısı 3'ün katıdır")



# Uygulama 3: 'sayilar' listesindeki tüm sayıların toplamı nedir?
toplam = 0          # Toplamı tutacak değişkene başta 0 değeri atanır

for e in sayilar:
    toplam += e

print(f"sayilar listesindeki tüm sayıların toplamı: {toplam}")




urunler = ["Oppo A5", "Oppo B6", "İphone C7", "İphone D8"]
# Aşağıdaki uygulamaları yukardaki urunler listesine göre yapınız

# Uygulama 1: 'urunler' listesindeki tüm İphone marka ürünleri listeleyiniz
for degisken in urunler:
    if degisken.startswith("İphone"):   # startswith() metodu ile İphone ile başlayan elemanlar seçildi
        print(degisken)



# Uygulama 2: 'urunler' listesinde kaç adet Oppo ürünü vardır?
urunAdedi = 0            # Toplam ürün sayısını tutacak değişkene başta 0 değeri atanır

for sayiDegiskeni in urunler:
    if sayiDegiskeni.startswith("Oppo"): # startswith() metodu ile Oppo ile başlayan elemanlar seçildi
        urunAdedi += 1                   # Ürün adedi sayısına 1 ekleniyor

print(f"Oppo Ürünlerinin Toplam Adedi: {urunAdedi}")
