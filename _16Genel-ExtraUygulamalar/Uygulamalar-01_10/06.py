
"""
    Kullanıcıdan bir metin alınız ve bu metni ters çevirerek ekrana yazdırınız.
"""

icerik = input("Bir metin giriniz: ")

tersIcerik = icerik[::-1]   # icerik değişkenini ters çevirip yeni değişekene (tersIcerik) atama

print(tersIcerik)
