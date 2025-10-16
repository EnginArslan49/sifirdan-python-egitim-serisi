
# Parametreli fonksiyonlar, dışarıdan veri (girdi) alarak işlem yapar.
# Bu sayede fonksiyon daha esnek, tekrar kullanılabilir ve dinamik olur.

#   YAPI:
#   def fonksiyon_adi(parametre1, parametre2, ...):
#     işlemler
#     return sonuç (isteğe bağlı)


# Örnek 1: İki sayıyı toplayan fonksiyon
def topla(a, b):
    sonuc = a + b
    print("Toplam:", sonuc)

topla(5, 8)  # a=5, b=8
# Çıktı: Toplam: 13



# Örnek 2: Kullanıcıdan alınan sayılarla çarpma işlemi
def carp(sayi1, sayi2):
    sonuc = sayi1 * sayi2
    print("Çarpım:", sonuc)

"""
   Kullanıcıdan veri alarak fonksiyona gönderilebilir
   x = int(input("1. sayıyı girin: "))
   y = int(input("2. sayıyı girin: "))
   carp(x, y)
"""



# Örnek 3: Metin birleştirme
def birlestir(ad, soyad):
    tam_isim = ad + " " + soyad
    return tam_isim

isim = birlestir("Arda", "Yılmaz")
print("Tam isim:", isim)
# Çıktı: Tam isim: Arda Yılmaz



# Örnek 4: Varsayılan parametreli fonksiyon
def selamla(isim="Engin Arslan"):  # eğer fonksiyona parametre verilmezse varsayılan "Engin Arslan" değeri atandı
    print("Merhaba,", isim)

selamla("Elif")     # Parametre verildi → "Merhaba, Elif"
selamla()           # Parametre verilmedi → varsayılan kullanılır → "Merhaba, Engin Arslan"



# Örnek 5: Birden fazla işlem yapan fonksiyon
def islem(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    return toplam, fark, carpim  # birden fazla değer döndürür

t, f, c = islem(10, 3)
print("Toplam:", t)
print("Fark:", f)
print("Çarpım:", c)


# NOT: Parametreler dışarıdan fonksiyona veri iletir.
"""
    Fonksiyon çağrılırken parametre sırası önemlidir.
    return ile hesaplanan sonuç dışarıya aktarılabilir.
"""
