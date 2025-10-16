
Baslik = "Karakter Dizileri Uygulama"

# 1. Uygulama: 'Baslik' değişkeni içerisindeki karakter sayısını ekrana yazdırın.
print(len(Baslik))  # Çıktı: 24


# 2. Uygulama: 'Baslik' içerisindeki 'Dizileri' kelimesini alın
dizi_kelimesi = Baslik[9:17] # 17. indeks dahil değil
print(dizi_kelimesi)  # Çıktı: Dizileri


# 3. Uygulama: 'Baslik' değişkenindeki ilk 5 ve son 5 karakteri ekrana yazdırın.
ilkBesKarakter = Baslik[:5]
sonBesKarakter = Baslik[-4:]
print(f"Dizinin ilk 5 karakteri {ilkBesKarakter}")  # Çıktı: Karak
print(f"Dizinin son 5 karakteri {sonBesKarakter}")  # Çıktı: lama


# 4. Uygulama: 'Baslik' değişkenindeki içeriği tersten ekrana yazdırın.
tersHali = Baslik[::-1]
print(f"String'in tersten yazılmış hali: {tersHali}")  # Çıktı: amaluypU ireliD rekatraK


