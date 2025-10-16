
"""
    Kullanıcıdan 2 değer isteyin klavyeden girilen bu değerleri veri tipi dönüşümü mantığında
    int() fonksiyonu ile string'den int'e çevirin ve sonucu ekrana yazdırın
"""

sayi1 = int(input("1. Sayıyı Giriniz: ")) # Girilen değeri int() fonksiyonu ile string'den int'e çevirdik
sayi2 = int(input("2. Sayıyı Giriniz: "))

print("İki Sayının Toplamı: " + str(sayi1+sayi2)) # Sonucu ekrana yazdırmak için str fonksiyonu ile int'den string'e çevirdik
