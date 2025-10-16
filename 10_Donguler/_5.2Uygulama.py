
"""
    UYGULAMA:
        Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
        ** dictionary liste yapısı (ogrNo, ogrAdi, ogrSoyadi) şeklinde olacak.
        ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.
"""

ogrenciler = []     # Kullanıcının girmiş olduğu öğrenci bilgilerini tutmak için gerekli listeyi oluşturduk ve başta boş değer verdik

istenenOgrenciSayisi = int(input("Kaç öğrenci ekleyeceksiniz? : ")) # Kullanıcının kaç öğrenci eklemek istediğini sorma (döngüde kullanılacak)
donguDegeri = 1            # Döngünün başlangıç değeri

while donguDegeri <= istenenOgrenciSayisi:
    ogrenciNo = int(input("Öğrenci No: "))
    ogrenciAdi = input("Öğrenci Adı: ")
    ogrenciSoyadi = input("Öğrenci Soyadı: ")

    ogrenciler.append(
        # ogrenciler listesine elemanları dictionary (key : value değerler) liste olarak ekliyoruz
        {
            "ogrNo" : ogrenciNo,
            "ogrAdi" : ogrenciAdi,
            "ogrSoyadi" : ogrenciSoyadi
        }
    )

    donguDegeri += 1    # Sonsuz döngüye girmemesi için donguDegeri değişkeninin değerini 1 arttırıyoruz

# Uygulama buraya gelince tüm öğrenci bilgileri eklenmiş demektir sıra girilen öğrenci bilgilerini ekrana yazdırma da
print(ogrenciler)
