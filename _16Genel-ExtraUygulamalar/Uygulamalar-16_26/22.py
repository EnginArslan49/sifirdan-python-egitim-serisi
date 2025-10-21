
"""
    Kullanıcıdan bir metin alınız ve metindeki tüm boşlukları kaldırarak ekrana yazdırınız.
"""

icerik = input("Boşlukları alınacak içeriği giriniz: ")

bosluklariAlinmis = icerik.split(" ")

icerikler = ""

for i in bosluklariAlinmis:
    if i in " ":
        continue
    else:
        icerikler += i


print(icerikler)
