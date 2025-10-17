
# Dosya yönetimi (File Management), programın dış dünyadaki dosyalarla (örneğin .txt, .csv, .json dosyaları) veri alışverişi yapmasını sağlar.
# Python'da dosya yönetimi için genellikle "open()" fonksiyonu kullanılır.

# Dosya işlemleri 4 temel adımdan oluşur:
#   Dosyayı açmak (open)
#   Dosyaya yazmak veya dosyadan okumak
#   İşlemleri tamamlamak
#   Dosyayı kapatmak (close)

"""
   Dosya açma biçimleri (modları):
    "r" → Sadece okuma (read)
    "w" → Yazma (varsa silip yeniden yazar)
    "a" → Ekleme (append)
    "x" → Yeni dosya oluşturma (varsa hata verir)
    "r+" → Hem okuma hem yazma
"""

# Basit örnek:
# dosya = open("veri.txt", "w")  # 'veri.txt' dosyasını yazma modunda açar
# dosya.write("Merhaba Python!") # Dosyaya metin yazar
# dosya.close()                  # Dosyayı kapatır

# Not:
# Dosya kapatılmazsa veriler tam yazılmayabilir veya dosya kilitlenebilir.
# Bu yüzden genelde "with open(...)" yapısı tercih edilir.
# Örnek:
# with open("veri.txt", "r") as dosya:
#     icerik = dosya.read()
#     print(icerik)


"""
    ÖZET:
    Dosya yönetimi = Verileri dış dosyalara kaydetme, okuma ve güncelleme işlemleridir.
    Gerçek dünyada log tutma, kullanıcı verisi saklama, rapor yazma gibi işlemlerde kullanılır.
"""
