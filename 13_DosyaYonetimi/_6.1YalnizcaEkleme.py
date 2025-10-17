
"""
    "a" MODU - SADECE EKLEME (APPEND)
    - Dosya yoksa OLUŞTURUR, varsa AÇAR
    - SADECE YAZMA işlemi yapılabilir, OKUMA YAPILAMAZ
    - Yazma işlemi HER ZAMAN DOSYANIN SONUNA eklenir
    - Dosya içeriği asla silinmez veya üzerine yazılmaz
    - Güvenli bir moddur - veri kaybı riski yoktur
"""

# Dosya yoksa oluşturur, varsa sonuna ekler
with open("_6.2log.txt", "a", encoding="utf-8") as dosya:
    dosya.write("İşlem tamamlandı: " + "2025-10-17" + "\n")

print("_6.2log.txt dosyasına yeni içerik eklendi")

# Her çalıştırmada yeni satırlar eklenir, eski içerik korunur