
# Fonksiyon çağırırken parametreleri isimleriyle (anahtar=değer şeklinde) verebiliriz.
# Bu, kodun okunabilirliğini artırır ve parametre sırası karışsa bile doğru eşleştirme yapılmasını sağlar.

#   YAPI:
#   fonksiyon_adi(parametre1=deger1, parametre2=deger2, ...)


# Örnek 1: Sıra önemli değil → isimlendirme kullanıldığı için doğru eşleşir
def bilgi(ad, yas, sehir):
    print(f"Ad: {ad}, Yaş: {yas}, Şehir: {sehir}")

# Parametreleri sırayla girebiliriz:
bilgi("Ayşe", 22, "İzmir")

# Ya da isimlendirerek farklı sırayla yazabiliriz:
bilgi(sehir="Ankara", ad="Mehmet", yas=30)

# Çıktı:
# Ad: Ayşe, Yaş: 22, Şehir: İzmir
# Ad: Mehmet, Yaş: 30, Şehir: Ankara


# Örnek 2: İsimlendirme + varsayılan değer bir arada
def mesaj_yaz(ad, mesaj="Hoş geldin!"):
    print(f"{ad}, {mesaj}")

mesaj_yaz("Ali")  # mesaj verilmedi → varsayılan değer kullanılır
mesaj_yaz(ad="Elif", mesaj="Python öğreniyor!")  # her iki parametre açıkça belirtilmiş

# Çıktı:
# Ali, Hoş geldin!
# Elif, Python öğreniyor!


# Örnek 3: Sayısal işlemlerde isimlendirilmiş parametre kullanımı
def carpma(a, b, c):
    sonuc = a * b * c
    print("Sonuç:", sonuc)

carpma(a=2, c=5, b=3)  # sıra değişse bile doğru hesap yapılır
# Çıktı: Sonuç: 30

"""
    NOT:
    İsimlendirilmiş parametreler, kodun okunabilirliğini artırır.
    Parametre sırası karışsa bile isimlendirme sayesinde hatasız çalışır.
    Zorunlu parametreler önce, isteğe bağlı (default) parametreler sonra tanımlanmalıdır.
"""
