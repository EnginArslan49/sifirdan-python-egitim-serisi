
"""
    Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız
        101 Yiğit Bilgi     2008    (75, 45, 80)
        102 Ahmet Bilgi     2015    (65, 70, 65)
        103 Ateş Kurnaz     2019    (89, 54, 90)
"""

ogrenciler = {
    101: {
        "ad": "Yiğit Bilgi",
        "dogumYili": 2008,
        "notlar": (75, 45,80)
    },
    102: {
        "ad": "Ahmet Bilgi",
        "dogumYili": 1999,
        "notlar": (65, 70,65)
    },
    103: {
        "ad": "Ateş Kurnaz",
        "dogumYili": 2019,
        "notlar": (89, 54,90)
    }

}

# Adım 2: Klavyeden girilen öğrenci numarasına göre aşağıdaki örnek cümleyi yazdırın
#           Cümle: {numara} numaralı {ad} ismindeki öğrencinin yaşı: {yas} ve not ortalaması: {ortalama}.

girilenNumara = int(input("Öğrenci Numarasını Giriniz: "))

ogrenci = ogrenciler[girilenNumara]  # Girilen öğrenci numarasına göre öğrencinin tüm bilgilerini seçme

ortalama = ( ogrenci["notlar"][0] + ogrenci["notlar"][1] + ogrenci["notlar"][2] ) / 3

print( f"{girilenNumara} numaralı {ogrenci["ad"]} ismindeki öğrencinin yaşı: {2025 - ogrenci["dogumYili"]} ve not ortalaması: {ortalama}." )
