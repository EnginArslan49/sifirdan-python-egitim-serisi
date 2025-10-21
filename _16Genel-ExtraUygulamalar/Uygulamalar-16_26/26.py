
"""
    Kullanıcıdan bir içerik alınız ve bu içerikteki tekrar eden elemanları bir kez olacak şekilde ekrana yazdırınız.
"""

icerik = input("Bir içerik giriniz: ").strip()  # Baş ve sondaki boşlukları kaldır

# Tekrarsız karakterleri bulmak için dict.fromkeys() kullanıyoruz
tekrarsizIcerik = " ".join(dict.fromkeys(icerik.replace(" ","")))  # benzersiz değerleri string olarak birleştiriyoruz

# Sonucu ekrana yazdır
print(f"Tekrarsız içerik: {tekrarsizIcerik}")


"""
    TEST:
        Girdi: Arslan Yazılım
        Çıktı: A r s l a n Y z ı m (Her karakter arasına boşluk koyar ve replace fonksiyonu ile kullanıcının vermiş olduğu içerikteki boşluklar kaldırılır, bu şekilde ilk boşluk elemanı da göz ardı edilir aksi halde program fazladan bir boşluk karakteri yazar)
"""
