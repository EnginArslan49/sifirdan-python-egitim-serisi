
# Parametresiz fonksiyonlar, dışarıdan herhangi bir veri (girdi) almaz.
# Tüm işlemler fonksiyonun içinde yapılır.
# Genellikle sabit işlemler veya kullanıcıdan veri alan durumlarda kullanılır.


# Örnek 1: Basit mesaj yazdırma
def selamla():
    print("Python Programlama Dili")

# Fonksiyon çağrılır
selamla()

# Çıktı: Python Programlama Dili



# Örnek 2: Kullanıcıdan veri alıp ekrana yazdırma
def bilgi_al():
    ad = input("Adınızı girin: ")
    print("Hoş geldin,", ad)

# Fonksiyon çağrılır (Fonksiyon çağrılmadan herhangi bir işlem yapmaz)
bilgi_al()



# Örnek 3: Sabit işlem yapan fonksiyon
def sabit_islem():
    sayi1 = 10
    sayi2 = 5
    sonuc = sayi1 * sayi2
    print("Çarpım sonucu: ", sonuc)

sabit_islem()

# Çıktı: Çarpım sonucu: 50


# NOT:
# - Parametre alınmaz, tüm değerler fonksiyon içinde tanımlanır.
#    return kullanılmazsa varsayılan olarak None döner.
#    Kod tekrarını azaltmak ve yapıyı düzenlemek için kullanışlıdır.
