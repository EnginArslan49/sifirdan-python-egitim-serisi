"""
    "a+" modu dosyayı hem okumak hem yazmak için kullanılır.
    - Dosya mevcut olmalıdır, yoksa hata verir.
    - İmleç (cursor) dosya başında başlar.
    - Yazma işlemi, mevcut içeriğe ekleme yani sonuna yazma işlemi yapar
    
    NOT: Dosya mevcut değilse 'FileNotFoundError' hatası oluşur.
"""

try:
    with open("_5.2log.txt", "a+", encoding="utf-8") as dosya:
        dosya.seek(0)  # İmleci dosya başına alır
        print("Dosya mevcut içeriği:")
        print(dosya.read())  # Önce mevcut içeriği okur

        dosya.seek(0)  # İmleci dosya başına alır
        dosya.write("Bu satır a+ ile yazıldı.\n")  # Mevcut içeriğin başını değiştirir
        print("\nYeni veri dosyaya yazıldı.")
except FileNotFoundError:
    print("HATA: '_5.2log.txt' dosyası bulunamadı. Lütfen dosyayı oluşturun.")

"""
    AÇIKLAMA:
    - "r+" → Hem okuma hem yazma için kullanılır.
    - seek(0) → Yazma konumunu dosya başına taşır.
    - write() → Dosyanın içeriğini baştan itibaren değiştirir.
"""
