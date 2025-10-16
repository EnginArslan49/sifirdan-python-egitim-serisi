
# *args, fonksiyona kaç tane parametre gönderileceğini bilmediğimiz durumlarda kullanılır.
# args bir "tuple" (demet) olarak gelir, yani birden fazla değeri tutabilir.

def topla(*args):
    print(args)            # args içindeki değerleri tuple olarak gösterir
    print(type(args))      # <class 'tuple'> şeklinde yazdırır
    toplam = 0
    for i in args:         # her parametreyi sırayla toplar
        toplam += i
    return toplam           # toplam sonucu geri döndürür

sonuc = topla(15, 30, 45, 60)  # kaç parametre gönderileceği fark etmez
print("Toplam:", sonuc)

"""
    ÇIKTI:
    (15, 30, 45, 60)
    <class 'tuple'>
    Toplam: 150
"""

"""
    NOT:
    *args, fonksiyona sınırsız sayıda parametre göndermeyi sağlar.
    args ismini değiştirebilirsiniz ama genelde *args kullanılır (Python standardıdır).
    Gelen veriler tuple olduğu için üzerinde döngü kurulabilir ama değiştirilemez.
"""
