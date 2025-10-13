

# String Birleştirme için 3 farklı yöntem vardır.
# 1. + Operatörü
isim = "Ahmet"
soyisim = "Yılmaz"
tam_isim = isim + " " + soyisim
print(tam_isim)


# 2. f-string (Python 3.6 ve üzeri)
ad2 = "Mehmet"
soyad2 = "Demir"
tam_ad2 = f"{ad2} {soyad2}"
print(tam_ad2)

# 3. format() metodu
# format() → String içinde değişkenleri yerleştirmek için kullanılır.
# {} süslü parantezler, yer tutucu (placeholder) görevi görür.

# Format metodunun 1. Basit kullanımı
isim = "Arda"
yas = 25
print("Adı: {}, Yaşı: {}".format(isim, yas))
# Çıktı: Adı: Arda, Yaşı: 25

# Format metodunun 2. Sıra numarası ile kullanımı
print("Yaşı: {1}, Adı: {0}".format(isim, yas))
# {0} → ilk değer, {1} → ikinci değer
# Çıktı: Yaşı: 25, Adı: Arda
