

kursAdi = "Arslan Yazılım ile Python Programlama Dersleri"
website = "https://arslanengin.com.tr"

# Uygulama 1: " Arslan Yazılım " karakter dizisinin baş ve sonundaki fazla boşlukları silip ekrana yazdırın (strip() metodu)
print(" Arslan Yazılım ".strip())

# Uygulama 2: kursAdi değişkenindeki tüm harfleri küçük harfe çevirin (lower() metodu)
print(kursAdi.lower())

# Uygulama 3: website değişkeni içinde kaç adet '.' karakteri vardır? (count() metodu)
print(website.count('.'))

# Uygulama 4: website değişkeni https ile mi başlıyor (startswith() metodu)
print(website.startswith("https"))  # Sonuç: True

# Uygulama 5: website değişkeni com ile mi bitiyor (endswith() metodu)
print(website.endswith(".com"))     # Sonuç: False

# Uygulama 6: kursAdi içerisindeki tüm değerler karakterlerden mi oluşuyor? (isalpha() metodu)
print(kursAdi.isalpha())    # Sonuç boşluklar olduğundan dolayı False gelir eğer boşluklar kaldırılırsa true gelir

# Uygulama 7: kursAdi değişkeni içerisindeki tüm boşlukları '-' ile değiştiriniz (replace() metodu)
print(kursAdi.replace(' ', '-'))

# Uygulama 8: kursAdi değişkeni içerisindeki Python kelimesini C# olarak değiştiriniz (replace() metodu)
print(kursAdi.replace('Python', 'C#'))

# Uygulama 9: website değişkeni 'www' değerini içeriyor mu?
 # Yöntem 1 (index() metodu ile) Değer string'de yoksa hata verir
#print(website.index("www"))
 # Yöntem 2 (find() metodu ile) Değer string'de yoksa -1 değerini döndürür
print(website.find("www"))

# Uygulama 10: kursAdi değişkenini listeye çeviriniz
liste = kursAdi.split(" ") # kursAdi string'ini boşluklardan ayırarak bir liste oluşturduk
print(liste[0])            # Oluşturulan listenin İLK elemanını yazdırma
print(liste[-1])           # Oluşturulan listenin SON elemanını yazdırma
