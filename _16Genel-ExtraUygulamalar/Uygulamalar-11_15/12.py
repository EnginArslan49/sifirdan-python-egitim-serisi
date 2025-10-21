
"""
    Kullanıcıdan bir metin alınız ve bu metindeki türkçe sesli harflerin sayısını ekrana yazdırınız.
"""

sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü", "A", "E", "I", "İ", "O", "Ö", "U", "Ü"] # Türkçe sesli harflerin olduğu liste hem büyük hem de küçük harfleri yakalaması için 2 formatta yazıldı. Büyük-küçük harflerin tamamını bir listede yazmak yerine lower veya upper metodu ile dönüşüm yapıp da kullanabilirsiniz

icerik = input("Sesli harfleri sayılacak metni giriniz: ")

sesliHarfAdedi = 0

for i in icerik:
    if i in sesliHarfler:
        sesliHarfAdedi += 1


if sesliHarfAdedi > 0:
    print(f"Girilen metindeki sesli harf adedi: {sesliHarfAdedi}")
else:
    print("Girilen metinde sesli harf YOK!")





"""
    GELİŞMİŞ VERSİYON:
        Kullanıcının girmiş olduğu metindeki sesli harf sayısı ve sesli harfleri gösterme
"""

sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü", "A", "E", "I", "İ", "O", "Ö", "U", "Ü"]

icerik = input("Sesli harfleri sayılacak metni giriniz: ")

sesliHarfListesi = []   # Başta Boş Varsa Eklenecek

for i in icerik:
    if i in sesliHarfler:
        sesliHarfListesi.append(i)


if sesliHarfAdedi > 0:
    benzersizSesliHarfler = list(dict.fromkeys(sesliHarfListesi))
    print(f"Girilen metindeki:\nSesli harf adedi: {len(sesliHarfListesi)}\nMetinde kullanılan benzersiz sesli harfler: {benzersizSesliHarfler}")
else:
    print("Girilen metinde sesli harf YOK!")
