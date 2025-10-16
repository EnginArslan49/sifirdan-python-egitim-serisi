
# Fonksiyonlar, belirli bir görevi yerine getiren, tekrar kullanılabilir kod bloklarıdır.
# "Bir işi bir kez tanımla, her yerde kullan" mantığıyla çalışır.
# Kod tekrarını azaltır, okunabilirliği ve bakımı kolaylaştırır.


# Fonksiyon Tanımlama Yapısı:
#   def fonksiyon_adi(parametre1, parametre2, ...):
#     yapılacak işlemler
#     return sonuç (isteğe bağlı)


# Örnek 1: Parametresiz fonksiyon
def selamla():
    print("Merhaba, ARSLAN YAZILIM Python Eğitimine Hoş Geldin!")

# Fonksiyonu çağırma
selamla()


# Örnek 2: Parametreli fonksiyon
def topla(a, b):
    return a + b  # iki sayının toplamını döndürür

sonuc = topla(5, 3)
print("Toplam: ", sonuc)


# Örnek 3: Varsayılan parametreli fonksiyon
def carp(a, b=2):  # b verilmezse varsayılan değer 2 alınır
    return a * b

print(carp(4))           # 4 * 2 = 8
print(carp(4, 5))  # 4 * 5 = 20


# Örnek 4: Geri değer döndürmeyen fonksiyon
def yazdir(metin):
    print("Yazı:", metin)

yazdir("ARSLAN YAZILIM (arslanengin.com.tr)")


# NOT:
# - Fonksiyonlar def anahtar kelimesiyle tanımlanır.
# - return ile dışarıya değer gönderilebilir.

"""
    KRİTİK NOKTA:
    Fonksiyon çağrılmazsa (çalıştırılmazsa) içindeki kodlar çalışmaz.
"""
