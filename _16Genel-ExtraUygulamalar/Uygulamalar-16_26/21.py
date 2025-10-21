
"""
    Kullanıcıdan bir sayı alınız ve bu sayının tersini (basamakları ters çevrilmiş) ekrana yazdırınız.
    Girilen değer sayısal değilse kullanıcıyı uyarınız ve tekrar giriş yapmasını sağlayınız.
"""

# UZUN (KARMAŞIK) YÖNTEM
while True:
    try:
        alinanSayi = input("Bir sayı giriniz: ")

        alinanSayi = int(alinanSayi)    # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        sayininBasamaklarininTersHali = []

        alinanSayi = str(alinanSayi)    # for değişkeninde kullanmak için alınan sayıyı string'e çevirme (daha önceden girilen içeriğin sayı olup olmadığını öğrenmek için int'e çevirmiştik).

        deger = -1

        for i in alinanSayi:
            sayininBasamaklarininTersHali.append(alinanSayi[deger])
            deger += -1

        print(f"Girilen {alinanSayi} sayısının basamakları ters çevrilmiş hali: {sayininBasamaklarininTersHali}")

        break

    except ValueError as hata:
        print("Lütfen sayısal değer giriniz!")
# Eğer herşey yolunda ise 517 değeri girilirse çıktı olarak (liste şeklinde) ['7', '1', '5'] değerini verir

"""
    517 değeri girilirse çıktı olarak (liste şeklinde) aşağıdaki gibi olacaktır
    ÇIKTI: Girilen 517 sayısının basamakları ters çevrilmiş hali: ['7', '1', '5']
"""





# KISA (KOLAY ANLAŞILABİLİR) YÖNTEM
while True:
    try:
        alinanSayi = input("Bir sayı giriniz: ")

        alinanSayi = int(alinanSayi)    # Burada program hata verirsek kullanıcı sayısal değer girmemiş demektir ve except bloğu çalışır

        alinanSayi = str(alinanSayi)    # Sayıyı ters çevirmek için alınan sayıyı string'e çevirme (daha önceden girilen içeriğin sayı olup olmadığını öğrenmek için int'e çevirmiştik).

        sayininBasamaklarininTersHali = alinanSayi[::-1]

        print(f"Girilen {alinanSayi} sayısının basamakları ters çevrilmiş hali: {sayininBasamaklarininTersHali}")

        break

    except ValueError as hata:
        print("Lütfen sayısal değer giriniz!")

"""
    517 değeri girilirse çıktı aşağıdaki gibi olacaktır
    ÇIKTI: Girilen 517 sayısının basamakları ters çevrilmiş hali: 715
"""
