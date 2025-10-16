
'''
    Bir değişkenin veri tipini öğrenmek için type() fonksiyonu kullanılır.
    type(değişken) → değişkenin veri tipini verir. Bu sayede kodun hangi türde veri ile çalıştığını kontrol edebilirsin.
'''

# Değişkenleri tanımlayalım
sayi = 10
fiyat = 19.99
isim = "Ahmet"
aktif_mi = True
meyveler = ["elma", "armut", "muz"]

# Veri tiplerini ekrana yazdıralım
print(type(sayi))       # <class 'int'>  → tam sayı
print(type(fiyat))      # <class 'float'> → ondalıklı sayı
print(type(isim))       # <class 'str'> → metin
print(type(aktif_mi))   # <class 'bool'> → doğru/yanlış
print(type(meyveler))   # <class 'list'> → liste

