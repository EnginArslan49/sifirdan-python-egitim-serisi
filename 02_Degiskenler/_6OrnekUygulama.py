'''

Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.

A) Toplam ödeme ücreti nedir?
B) Ödenen miktarın kdv oranı nedir? (%18)

MÜŞTERİ BİLGİLERİ
    Engin Arslan
    0555 222 3344
    info@enginarslan.com
    Bitlis

SATIN ALINAN ÜRÜNLER

    Ürün Adı: Kablosuz Mouse
    Fiyat: 	  550 ₺

    Ürün Adı: Kablosuz Klavye
    Fiyat: 	  650 ₺

    Ürün Adı: Dizüstü Bilgisayar
    Fiyat: 	  55.000 ₺

'''



# ÇÖZÜM
ad = "Engin Arslan"
telefon = "0555 222 3344"
gmail = "info@enginarslan.com"
il = "Bitlis"

urun1Ad = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosuz Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55_000 # araya . işareti ile ayrıla yapılmaz => 55.000: YANLIŞ
                    # Python'da binlik ayırıcı olarak _ kullanılabilir: 55_000

toplamOdenenUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat

print("Toplam Ödenecek Tutar: ", toplamOdenenUcret)

kdv = toplamOdenenUcret * 0.18 # Toplam Ürün Fiyatını 0.18 ile çarparak %18 KDV oranı bulunur
print("Ödenen Miktarın KDV Oranı: ", kdv)