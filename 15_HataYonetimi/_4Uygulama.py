from http.cookiejar import time2isoz

icerikler = ["1", "kd", "23", "5", "ea", "dfs", "99"]
# Aşağıdaki uygulamaları yukardaki listeye göre yapınız.

# Uygulama 1: Liste elemanları içindeki sayısal değerleri bulunuz

for i in icerikler: # icerikler adlı listenin elemanlarını tamamen dolaşan for döngüsü
    try:
        sonuc = int(i)  # Gelen i değeri int'e çevrilebiliyorsa sayıdır,
        print(sonuc)    # ekrana yazdırılır
    except ValueError:
        continue        # Gelen i değeri int'e çevrilemiyordur. continue ile bir sonraki tura geçilir





# Uygulama 2: Kullanıcı 'q' tuşuna basmadıkça aldığınız her klavye girdisinin sayı olduğundan emin olunuz aksi halde hata mesajı yazınız (Girilen içerik sayı ise girdi almaya devam etsin).

tus = ""

while tus != "q":
    girilenDeger = input("Bir değer giriniz: ")

    if girilenDeger == "q":
        print("'q' tuşuna basarak programı kapattınız!")
        break

    try:
        kontrol = float(girilenDeger) # Girilen değer ondalıklı sayıya dönüştürülür eğer ondalıklı sayıya dönüştürülemiyorsa program hata verir programın işleyişi bozulmadan except bloğu çalışır
        # Püf Nokta: Girilen değer int'e de çevrilebilir fakat kullanıcının 10.8 gibi ondalıklı bir sayı girmesine karşın float'a dönüştürdük. Eğer ki int tipine dönüştürmüş olsaydık kullanıcı 10.8 gibi ondalıklı bir sayı girdiği zaman bu değer sayı olmasına rağmen int'e çevrilemeyeceğinden uygulama except bloğuna geçerek uygulamayı sonlandırır

    except ValueError:
        print(f"Girdiğiniz '{girilenDeger}' içeriği sayısal bir değer olmadığından program sonlandı.")
        break




# Uygulama 3: Dictionary ve key bilgilerini parametre olarak alan bilgileriGetir(liste, deger) fonksiyonunu yazınız

urun = {"urunAdi":"Samsung S20"}

def bilgileriGetir(liste, deger):
    try:
        return liste[deger]
    except KeyError:
        return "YOK!"

print(bilgileriGetir(urun, "urunAdi"))

"""
    bilgileriGetir(urun, "urunAdi") # ÇIKTI: Samsung S20
    bilgileriGetir(urun, "fiyat")   # ÇIKTI: YOK
"""
