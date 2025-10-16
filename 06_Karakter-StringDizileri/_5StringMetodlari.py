from encodings.punycode import adapt

mesaj = "ARSLAN YAZILIM Python Eğitimi"

# upper() metodu ile tüm string değerini büyük harflere dönüştürülür
buyukHarf = mesaj.upper()

# lower() metodu ile tüm string değerini küçük harflere dönüştürülür
kucukHarf = mesaj.lower()

# title() metodu ile tüm string değerin yalnızca baş harfleri büyük harflere dönüştürülür
baslikHarfleriBuyuk = mesaj.title()

# capitalize() metodu ile string değerinin yalnızca baş harfi büyük harflere dönüştürülür
yalnizcaBasHarfBuyuk = mesaj.capitalize()


#######################################################################################
takmaAd = "arslan"

# isupper() metodu ile string değerinin büyük harf olup olmadığını sorarız sonuç bool yani true (evet) ya da false (hayır) değer döndürür
buyukHarfMi = takmaAd.isupper()
print(buyukHarfMi)  # Sonuç: False
# ÖNEMLİ NOT: Yalnızca 1 harfe değil tüm string değerine bakar ve ona göre değer döndürür

# islower() metodu ile string değerinin küçük harf olup olmadığını sorarız sonuç olarak bool değer döndürür
kucukHarfMi = takmaAd.islower()
print(kucukHarfMi)  # Sonuç: True
#######################################################################################


email = " abc@gmail.com "
bosluklardanArindirilmis = email.strip() # strip() metodu ile değişkenin başında ve sonundaki fazla boşluklar alınır

# split() metodu ile değişken belirtilen parametreye göre birbirinden ayrılır. Eğer ki split metoduna parametre verilmezse bu boşluklardan ayır anlamına gelir
# Örnek:
stringDeger = "Arslan Yazılım Web & Özel Otomasyon Çözümleri Hizmeti Veren Bir Firmadır"
ayirma = stringDeger.split('&') # Strin değeri & karakterinden ayırdık
print(ayirma)   # Sonuç: ['Arslan Yazılım Web ', ' Özel Otomasyon Çözümleri Hizmeti Veren Bir Firmadır']


# index() metodu ile string değer içinde belirtilen kelime veya harfin kaçıncı indekste olduğu bulunabilir
icerik = "ARSLAN YAZILIM Python Eğitimi"
deger = icerik.index("Python") # icerik string'i içerisinde Python kelimesini arama
print(deger) # icerik string'inde Python kelimesi ilk olarak (baş harfi) 15. indekste geçtiğinden 15 değerini döndürür
# ÖNEMLİ NOT: index() metodu ile arama yapılıyorsa aranan kelime veya karakter yoksa hata verir

# find() metodu ile string değer içinde belirtilen kelime veya harfin kaçıncı indekste olduğu bulunabilir
icerik2 = "ARSLAN YAZILIM Python Eğitimi"
deger2 = icerik.find("Python") # icerik string'i içerisinde Python kelimesini arama
print(deger2) # icerik string'inde Python kelimesi ilk olarak (baş harfi) 15. indekste geçtiğinden 15 değerini döndürür
# ÖNEMLİ NOT: find() metodu ile arama yapılıyorsa aranan kelime veya karakter yoksa geriye -1 değerini döndürür

# startswith() metodu ile string değer belirtilen karakter veya string değer ile mi BAŞLIYOR bakılır. Sonuç bool (True/False) tipinde döner
alfabe = "abcdef"
aIleMiBasliyor = alfabe.startswith('a') # True
bIleMiBasliyor = alfabe.startswith('b') # False

# endswith() metodu ile string değer belirtilen karakter veya string değer ile mi BİTİYOR bakılır. Sonuç bool (True/False) tipinde döner
dIleMiBitiyor = alfabe.endswith('d')     # False
fIleMiBitiyor = alfabe.endswith('f')     # alfabe değişkeni f karakteri ile bittiğinden sonuç True döner
# ÖNEMLİ NOT: startswith() metodu ile sorgulama yaparken küçük-büyük harf duyarlılığı vardır bu nedenle A ile a değerleri birbirinden farklıdır


# replace() metodu ile string değer içerisinden belirtilen kelime veya karakteri istenilen kelime veya karaktere çevrilebilir
# Örnek:
ilIlce = "Ağrı, Muş, Bitlis, Iğdır"
degistirme = ilIlce.replace("Bitlis", "Ahlat") # İlk parametre değiştirilecek olan değer 2.si ise yerine gelecek olan değer
print(degistirme) # Sonuç: Ağrı, Muş, Ahlat, Iğdır


# count() metodu ile bir string değer içerisinde kaç adet belirtilen karakter var bulunur
website = "https://arslanengin.com.tr"
print(website.count('.'))

# isalpha() metodu ile bir string değer yalnızca karakterlerden (harfler) mi oluşuyor kontrol etmek için kullanılır. Sonuç bool (True, False) tipinde döner
renk = "Kırmızı"
harflerdenMiOlusuyor = renk.isalpha()
print(harflerdenMiOlusuyor) # Sonuç: True