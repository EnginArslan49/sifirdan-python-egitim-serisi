
"""
    Bir dosyadaki verileri okumak için open() fonksiyonu kullanılır.
    Bu fonksiyon, diskteki dosyayı RAM’e getirerek Python içinde işlem yapmamızı sağlar.
    Dosya okuma işlemi için erişim modu olarak "r" (read) kullanılır.
    Dosya belirtilen konumda yoksa hata (FileNotFoundError) oluşur.
"""

dosya = open("_2.2log.txt", "r")    # Dosyayı okuma modunda açar
icerik = dosya.read()            # Dosyanın tamamını okur
print(icerik)                    # İçeriği ekrana yazdırır
dosya.close()                    # Dosyayı kapatır



"""
    seek(x) → Dosya imlecini belirtilen konuma taşır.
    Bu sayede dosya içinde istediğimiz yerden okumaya başlayabiliriz.
"""

dosya = open("_2.2log.txt", "r", encoding="utf-8")  # encoding="utf-8" → Türkçe karakterlerin doğru görüntülenmesi için kullanılır.
dosya.seek(0)                                       # İmleci dosya başına taşır
print(f"Dosyanın ilk satırı: {dosya.readline()}")   # İlk satırı okur
dosya.close()
"""
    - "r" modu sadece okuma işlemleri içindir.
    - Dosya yoksa hata verir.
    - with open() en güvenli yöntemdir.
    - seek() imleç konumunu değiştirir.
"""
