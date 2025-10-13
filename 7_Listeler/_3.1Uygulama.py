
# Uygulama 1: "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]

# Uygulama 2: Liste kaç elemanlıdır?
elemanSayisi = len(markalar)
print(elemanSayisi)

# Uygulama 3: Listenin ilk ve son elemanı nedir?
ilkEleman = markalar[0]
sonEleman = markalar[-1]

print(ilkEleman)
print(sonEleman)

# Uygulama 4: "Renault" markasını "Hyundai" ile güncelleyiniz
markalar[2] = "Hyundai"
print(markalar)

# Uygulama 5: "Seat" listenin bir elemanı mıdır?
seatElemanMidir = "Seat" in markalar
print(seatElemanMidir)

# Uygulama 6: Listenin ilk 2 elemanını alınız
ilk2Eleman = markalar[0:2] # 2 dahil değil (Yalnızca 0 ve 1. elemanlar)
print(ilk2Eleman)

# Uygulama 7: Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz
markalar = markalar + ["Ford", "Citroen"] # markalara önceki değerin üstüne yeni 2 değer ekleme
print(markalar)

# Uygulama 8: Listenin son elemanını siliniz
del markalar[-1]
print(markalar)
