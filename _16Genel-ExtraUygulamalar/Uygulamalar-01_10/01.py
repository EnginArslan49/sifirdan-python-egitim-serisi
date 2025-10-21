
"""
    Kullanıcıdan adınızı alınız ve ekrana "Merhaba <ad>!" ifadesini yazdırınız.
    Girdi boş veya geçersiz ise kullanıcıyı geçerli bir ad giriniz şeklinde uyarınız.
"""

ad = input("Adınız? : ").strip()    # strip() ile baş ve sondaki boşluk karakterleri alınır

while not ad:   # ad değişkeni boş veya boşluk karakteri olduğu sürece çalışan döngü
    print("Lütfen Adınızı Giriniz!")
    ad = input("Adınız? : ").strip()

print(f"Merhaba {ad}")
