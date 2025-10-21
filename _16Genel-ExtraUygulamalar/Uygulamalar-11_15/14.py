
"""
    Kullanıcıdan bir metin alınız ve bu metindeki tekrar eden karakterleri bir kez olacak şekilde ekrana yazdırınız.
"""

icerik = input("Tekrar eden karakter analizi yapılacak metni giriniz: ").strip()

# icerik değişkeni boş veya boşluk karakteri değilse
if icerik != "" and icerik != " ":
    tekrarsizIcerik = list(dict.fromkeys(icerik))   # dict.fromkeys(icerik) ile icerik değişkenindeki benzersiz değerler bulunur ve yeni değişkene (tekrarsizIcerik) atanır

    print(tekrarsizIcerik)  # Metindeki boşlukda bir karakter olarak algılanır bu sebeple boşluk karakteri de yazılır. Herhangi bir işleme tabi tutulacaksa boşluğun göz ardı edilmesi için harici kod yazılması gerekmektedir
else:
    print("Lütfen bir içerik girip tekrar deneyiniz!")
