
"""
    Bir dosyaya veri yazmak için "w", "a" veya "r+" modları kullanılır.
    - "w" : Yeni dosya oluşturur, varsa içeriği siler.
    - "a" : Dosya varsa sonuna ekleme yapar.
    - "r+" : Dosyayı hem okumak hem yazmak için açar.
"""

# Örnek 1: Yeni dosya oluşturup içine yazma
with open("_4.2log.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Python dosyaya veri yazma örneği.\n")
    dosya.write("Bu satır dosyaya kaydedildi.\n")

print("_4.2log.txt dosyası oluşturuldu ve veri yazıldı.")



# "a" modu, dosyayı silmeden sonuna yeni veri ekler.
with open("_4.2log.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Yeni satır eklendi.\n")

print("_4.2log.txt dosyasına yeni satır eklendi.")



"""
    - write() → Tek satır veya string yazar.
    - writelines() → Birden fazla satırı liste olarak yazar.
"""

satirlar = ["1. satır\n", "2. satır\n", "3. satır\n"]

with open("_4.2log.txt", "a", encoding="utf-8") as dosya:
    dosya.writelines(satirlar)

print("_4.2log.txt dosyasına birden fazla satır yazıldı.")
