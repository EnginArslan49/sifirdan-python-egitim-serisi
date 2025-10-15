
urunler = [
    {"urunAdi": "HP Victus 1", "fiyat" : 32999},
    {"urunAdi": "Lenovo Thinkpad", "fiyat": 25499},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "Huawei Matebook", "fiyat": 26999},
    {"urunAdi": "HP Victus 2", "fiyat" : 34999},
    {"urunAdi": "Casper Nirvana", "fiyat": 20000},
]
# Aşağıdaki uygulamaları yukardaki urunler listesine göre yapınız


# Uygulama 1: Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız
#               Cümle: {urunAdi} marka ürünün fiyatı {fiyat} liradır
for urun in urunler:
    print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} liradır")



# Uygulama 2: Ürünlerin fiyat toplamları nedir?
toplam = 0              # Toplam fiyatı tutacak değişkene başta 0 değeri atandı
for fiyat in urunler:
    toplam += fiyat["fiyat"]

print(f"Tüm ürünlerin toplam fiyatı: {toplam}")



# Uygulama 3: 25000 ile 40000 arasındaki ürünleri listeleyiniz
for filtre in urunler:
    if ( filtre["fiyat"] >= 25000 ) and ( filtre["fiyat"] <= 40000 ):
        print("25000 - 40000 arası ürün: ",filtre["urunAdi"])



# Uygulama 4: Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz (Kullanıcı urunAdi yazarsa tüm ürün adları, fiyat yazarsa tüm ürünlerin fiyat listesi çıksın)
anahtarKelime = input("Anahtar Kelime? : ")

for urunListeleme in urunler:
    print(urunListeleme[anahtarKelime])



# Uygulama 5: Kullanıcı alınan ürün adına göre o ürün adındaki tüm ürünleri listeleyiniz
urunAdi = input("Ürün Adı: ")

for filtreUrunAdi in urunler:
    if filtreUrunAdi["urunAdi"].lower().find(urunAdi.lower()) > -1:     # Sonuç -1'den büyükse en az 1 sonuç var anlamına gelir
        print(filtreUrunAdi["urunAdi"])             # Yalnızca ürün adını yazdırma eğer ki ürünün tüm bilgileri yazdırılmak istenirse filtreUrunAdi yazmak yeterlidir