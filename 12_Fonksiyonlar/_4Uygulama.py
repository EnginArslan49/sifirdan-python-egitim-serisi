
# Uygulama 1: Kendisine verilen bir kelimeyi ekrana belirtilen miktarda yazan fonksiyonu yazınız
def belirtilenSayiKadarKelimeYazdir(kelime, adet):
    for icerik in range(1, adet+1):         # son değer dahil olmadığı için adet+1 parametresi verildi
        print(f"{icerik}. Engin")

belirtilenSayiKadarKelimeYazdir("Engin", 5)




# Uygulama 2: Diktörtgen alan ve çevresini hesaplayan fonksiyonu yazınız
"""
    Alan Formülü: Kısa Kenar * Uzun Kenar
    Çevre Formülü: 2 * (Kısa Kenar + Uzun Kenar)
"""

def alanveCevreHesapla(kisaKenar, uzunKenar):
    alan = kisaKenar * uzunKenar
    cevre = 2 * (kisaKenar + uzunKenar)
    return f"Alan: {alan}, Çevre: {cevre}"

print( alanveCevreHesapla(5, 5) )




# Uygulama 3: Kendisine gönderilen 1 sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız

def tamSayiBolenBul(sayi):
    print(f"{sayi} sayının tam bölenleri")

    tamBolenler = []                # tam bölen sayıları tutmak için liste oluşturduk ve başta boş değer verdik

    for artis in range(2, sayi+1):  # son değer dahil olmadığı için sayi+1 yazıldı
        if sayi % artis == 0:
            tamBolenler.append(artis)

    return tamBolenler

print(tamSayiBolenBul(20))
