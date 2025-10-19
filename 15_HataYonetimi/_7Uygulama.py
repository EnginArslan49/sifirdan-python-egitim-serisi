
# Uygulama 1: Bir faktöriyel hesaplama fonksiyonu yazınız oluşturunuz ve fonksiyona gelen değer için hata mesajları tanımlayınız.

def faktoriyelHesapla(sayi):
    sayi = int(sayi)

    if sayi <= 0:
        raise ValueError("Değer 0 veya negatif olamaz!")

    sonuc = 1

    for i in range(1, sayi + 1):
        sonuc = sonuc * i

    return f"Girilen {sayi} sayısının faktöriyeli: {sonuc}"


try:
    print(faktoriyelHesapla(-41))
    print(faktoriyelHesapla(3))
except Exception as hata:
    print(f"Hata Yakalandı! {hata}")

print(faktoriyelHesapla(5))




# Uygulama 2: Girilen parola içerisinde türkçe karakter varsa hata veriniz

parola = input("Parolanızı Giriniz: ")

try:
    for i in parola:
        if i in ["İ", "Ö", "Ü", "Ş", "Ç", "Ğ", "ı", "ö", "ü", "ş", "ç", "ğ"]:
            raise ValueError("Türkçe Karakter Hatası")

except Exception as hata:
    print(f"GEÇERSİZ PAROLA\nGirilen {parola} parolasında türkçe karakterler var!")

else:
    print(parola)




# Uygulama 3: (GELİŞMİŞ VERSİYON) Girilen parola içerisinde türkçe karakter varsa hata veriniz. Parolada bulunan tüm türkçe karakterleri gösteriniz

turkceKarakterler = ["İ", "Ö", "Ü", "Ş", "Ç", "Ğ", "ı", "ö", "ü", "ş", "ç", "ğ"]    # Türkçe karakterleri tutan liste

def parolaKontrol(sifre):
    bulunan_karakterler = []    # Türkçe karakter varsa tutan liste

    # Tüm Türkçe karakterleri bul
    for karakter in sifre:
        if karakter in turkceKarakterler:
            bulunan_karakterler.append(karakter)

    # Eğer Türkçe karakter varsa exception fırlat
    if bulunan_karakterler:
        raise TypeError(f"Türkçe karakterler bulundu: {bulunan_karakterler}")

    return f"PAROLA GEÇERLİ! : {sifre}"


parola = input("Parolanızı Giriniz: ")

try:
    sonuc = parolaKontrol(parola)
    print(sonuc)
except Exception as hata:
    print(f"GEÇERSİZ PAROLA: {hata}")
