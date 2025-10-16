
# Tuple (demet), listelere benzer ama DEĞİŞTİRİLEMEZ bir veri yapısıdır.
# Yani oluşturulduktan sonra eleman ekleme, silme veya değiştirme (CRUD İşlemleri) yapılamaz.
# Parantez () ile tanımlanılır.

# 1. Tuple tanımlama
renkler = ("kırmızı", "yeşil", "mavi")

# 2. Tuple elemanlarını ekrana yazdırma
print(renkler)

# 3. Belirli elemana erişim (indeks 0’dan başlar)
print(renkler[0])   # "kırmızı"
print(renkler[-1])  # "mavi"

# 4. Uzunluğu öğrenme
print("Eleman sayısı:", len(renkler))  # 3

# 5. Tuple içinde arama
print("yeşil" in renkler)  # True
print("mor" in renkler)    # False

# 6. Tuple'dan listeye dönüştürme (değiştirilebilir hale getirmek için)
liste_renkler = list(renkler) # list() metodu ile tuple listeye çevrildi bu şekilde değiştirilebilir hale geldi
liste_renkler.append("sarı")  # Artık ekleme yapılabilir
print("Listeye dönüştürülmüş tuple:", liste_renkler)

# 7. Listeyi tekrar tuple’a dönüştürme
yeni_tuple = tuple(liste_renkler)
print("Tekrar tuple haline getirildi:", yeni_tuple)

# 8. Tek elemanlı tuple tanımlama (virgül şart!)
tek_renk = ("beyaz",)
print(type(tek_renk))  # <class 'tuple'>

# 9. Elemanlara dilimleme ile erişim
print(renkler[0:2])  # ('kırmızı', 'yeşil')

# 10. Tuple’ları birleştirme
renkler2 = ("mor", "turuncu")
birlesik = renkler + renkler2
print("Birleşmiş tuple:", birlesik)


# TUPLE METOTLARI: 2 adet Tuple metodu vardır
# 1. count() metodu
tupleListem = ("Dizüstü Bilgisayar", "Fare", "Mouse", "Fare")
print( tupleListem.count("Fare") ) # count() metodu ile tupleListem adındaki listede Fare string değerini arama
# Sonuç: 2

# 2. index() metodu
print( tupleListem.index("Mouse") )  # count() metodu ile tupleListem adındaki listede Mouse string değerinin indeks değerini arama
# Sonuç: 2