
"""
    Kullanıcıdan yaşınızı alınız ve 18’den küçükse “Reşit değilsiniz”, aksi halde “Reşitsiniz” ifadesini ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

while True:
    yas = input("Yaşınızı Giriniz: ")

    try:
        yas = int(yas)  # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        if yas < 18:
            print(f"Yaşınız: {yas} => Reşit değilsiniz")
        else:
            print(f"Yaşınız: {yas} => Reşitsiniz")

        break

    except ValueError as hata:
        print(f"Lütfen yaşınızı sayısal biçimde doğru yazdığınızdan emin olup tekrar deneyiniz!\nHata: {hata}\n")
