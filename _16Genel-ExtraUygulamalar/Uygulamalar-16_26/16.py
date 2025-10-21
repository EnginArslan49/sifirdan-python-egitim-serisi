
"""
    Kullanıcıdan bir cümle alınız ve cümledeki kelimeleri tek tek ekrana yazdırınız.
    Kelimeler arasındaki boşlukları dikkate alınız.
"""

alinanIcerik = input("Bir cümle giriniz: ")

bosluklardanAyrilmisDizi = alinanIcerik.split(" ")  # Kullanıcının girmiş olduğu girdiyi boşluklardan ayırıp tanımlanan yeni liste değişkene (bosluklardanAyrilmisDizi) atama

print("Boşluklardan ayrılmış cümleniz: ")

for i in bosluklardanAyrilmisDizi:
    print(i)
