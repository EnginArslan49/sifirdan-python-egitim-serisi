
# Fonksiyon tanımlarken parametrelere varsayılan (default) değer verebiliriz.
# Böylece fonksiyon, o parametre için değer girilmezse varsayılanı kullanır.

#   YAPI:
#   def fonksiyon_adi(parametre = varsayilan_deger):
#     işlemler


# Örnek 1: Basit selamlama fonksiyonu
def selamla(isim="Ziyaretçi"):
    print("Merhaba,", isim)

selamla("Ahmet")  # Parametre verildi → "Ahmet" kullanılır
selamla()         # Parametre verilmedi → "Ziyaretçi" kullanılır

# Çıktı:
# Merhaba, Ahmet
# Merhaba, Ziyaretçi


# Örnek 2: Toplama fonksiyonu (bir parametre eksikse varsayılan devreye girer)
def topla(a, b=10):
    sonuc = a + b
    print("Toplam:", sonuc)

topla(5, 3)  # a=5, b=3 → 8
topla(7)     # a=7, b varsayılan 10 → 17

# Çıktı:
# Toplam: 8
# Toplam: 17


# Örnek 3: Birden fazla varsayılan değerli parametre
def bilgi(ad="Bilinmiyor", yas=0, sehir="Tanımsız"):
    print(f"Ad: {ad}, Yaş: {yas}, Şehir: {sehir}")

bilgi("Elif", 25, "İzmir")  # tüm parametreler verildi
bilgi("Ali", 30)                  # sehir belirtilmedi → varsayılan değer kullanılır
bilgi()                                   # hiçbir parametre verilmedi → hepsi varsayılan olur

# Çıktı:
# Ad: Elif, Yaş: 25, Şehir: İzmir
# Ad: Ali, Yaş: 30, Şehir: Tanımsız
# Ad: Bilinmiyor, Yaş: 0, Şehir: Tanımsız

"""
    NOT:
    Varsayılan değerli parametreler, her zaman *normal parametrelerden sonra* yazılmalıdır. (Yani önce zorunlu, sonra varsayılan değerli parametreler gelir.)
    Bu özellik, fonksiyonu esnek hale getirir ve gereksiz parametre girişi zorunluluğunu ortadan kaldırır.
"""
