
musteriler = ["enginarslan", "yesimuzun", "safakaltiner", "gumuskumru"]
siparisToplamlari = [12000, 13000, 5000, 15000]
# Aşağıda verilen soruları yukardaki listelere göre yapınız

# Uygulama 1: 'enginarslan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz
#               enginarslan değeri tekrardan musteriler listesine, 5000 ise siparisToplamlari listesine eklenecek
musteriler.append("enginarslan")
siparisToplamlari.append(5000)

# Ekrana Yazdırma
print(musteriler)
print(siparisToplamlari)


# Uygulama 2: Son eklenen siparişi siliniz
#               enginarslan değeri musteriler listesinden, 5000 ise siparisToplamlari listesinden silinecek
musteriler.pop(-1)
siparisToplamlari.pop(-1)

# Ekrana Yazdırma
print(musteriler)
print(siparisToplamlari)


# Uygulama 3: Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız
#               'username' isimli müşterinin sipariş toplamı '<siparisToplam>' liradır
enginarslanBilgi = f"{musteriler[0]} isimli müşterinin sipariş toplamı {siparisToplamlari[0]} liradır"
yesimuzunBilgi = f"{musteriler[1]} isimli müşterinin sipariş toplamı {siparisToplamlari[1]} liradır"
safakaltinerBilgi = f"{musteriler[2]} isimli müşterinin sipariş toplamı {siparisToplamlari[2]} liradır"
gumuskumruBilgi = f"{musteriler[3]} isimli müşterinin sipariş toplamı {siparisToplamlari[3]} liradır"

# ÖNEMLİ NOT: Normalde yukardaki gibi kullanıcıların bilgileri tek tek yazılmaz henüz döngüler konusunu görmediğimiz için tek tek değer atama yolunu seçtik

# Ekrana Yazdırma
print(enginarslanBilgi)
print(yesimuzunBilgi)
print(safakaltinerBilgi)
print(gumuskumruBilgi)

# Uygulama 4: Müşterileri alfabetik olarak sıralayınız
musteriler.sort()
print(musteriler)


# Uygulama 5: Sipariş toplamlarını artan şekilde sıralayınız
siparisToplamlari.sort()
print(siparisToplamlari)


# Uygulama 6: Sipariş toplamlarını azalan şekilde sıralayınız
siparisToplamlari.sort(reverse=True) # sort ile önce artan şekilde sıralayıp verilen reverse=True parametresi ile de ters çevirmiş oluruz. Bu şekilde azalan yöntem olur
print(siparisToplamlari)


# Uygulama 7: En düşük sipariş hangisidir?
enDusukSiparis = min(siparisToplamlari)
print(enDusukSiparis)


# Uygulama 8: En yüksek sipariş hangisidir?
enYuksekSiparis = max(siparisToplamlari)
print(enYuksekSiparis)


# Uygulama 9: 'enginarslan' isimli kullanıcının kaç adet siparişi vardır?
enginarslanSiparisAdedi = musteriler.count("enginarslan")
print(enginarslanSiparisAdedi)


# Uygulama 10: musteriler listesinden "safakaltiner" isimli kullanıcıyı siliniz
musteriler.remove("safakaltiner")
print(musteriler)


# Uygulama 11: Listelerdeki tüm elemanları siliniz
musteriler.clear()
print(musteriler)

siparisToplamlari.clear()
print(siparisToplamlari)


# Uygulama 12: Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz
kullaniciAdi = input("Kullanıcı Adını Giriniz: ")
siparisToplam = input("Sipariş Toplam Tutarını Giriniz: ")

musteriler.append(kullaniciAdi)
siparisToplamlari.append(siparisToplam)

print(musteriler)
print(siparisToplamlari)