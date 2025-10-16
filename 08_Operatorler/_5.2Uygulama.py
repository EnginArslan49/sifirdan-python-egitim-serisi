from platform import android_ver

# Uygulama 1: Yaşı 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz
yas = 18
veliIzni = False

calismaDurumu = (yas >= 18) or (veliIzni == True)           # or (veya) kullandığımızdan her iki durumdan biri doğru olursa sonuç True gelir ve bu da bir işte çalışabileceği anlamını taşır. >= dediğimiz için ise yaş 18 olsa da True değerini alır
print(f"Kişi herhangi bir işte çalışabilir mi? : {calismaDurumu}")



# Uygulama 2: Ders notu 50-100 ise geçti değilse kalsın bilgisini yazdıran program
dersNotu = int(input("Ders Notunuz? : "))

gecmeKalmaDurumu = (dersNotu >= 50) and (dersNotu <= 100)
print(f"Öğrenci {dersNotu} ile dersten geçti mi? : {gecmeKalmaDurumu}")



# Uygulama 3: Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz
notOrtalamasi = float(input("Ortalamanız? : "))
zayif = 0

belgeAlmaDurumu = (notOrtalamasi >= 70) and (zayif == 0)
print(f"Öğrenci {notOrtalamasi} not ortalaması ile teşekkür belgesi alabiliyor mu? : {belgeAlmaDurumu}")



# Uygulama 4: İşe girmek için en az ÖnLisans ya da Lisans mezunu olma ve sigara içmeme durumunu kontrol ediniz
mezuniyet = "ÖnLisans"
sigara = True

iseGirebilmeDurumu = ( (mezuniyet == "ÖnLisans") or (mezuniyet == "Lisans") ) and sigara == False
print(f"Kişi {mezuniyet} mezuniyeti ile işe girebilir mi? : {iseGirebilmeDurumu}")



# Uygulama 5: Uygulama giriş kontrolünü (kullaniciAdi veya ePosta) ve parola için yapalım
kullaniciAdi = "yasarBilgin"
ePosta = "info@yasarbilgin.com"
parola = "1234"

girilenKullaniciAdiveyaEPosta = input("Kullanıcı Adı veya E-Posta: ")
girilenParola = input("Parola: ")

girisBasariliMi = ( (kullaniciAdi == girilenKullaniciAdiveyaEPosta) or (ePosta == girilenKullaniciAdiveyaEPosta) ) and (parola == girilenParola)
print(f"Giriş başarılı mı? : {girisBasariliMi}")