
# **kwargs, fonksiyona değişken sayıda "isimli" (anahtar=değer) parametre göndermek için kullanılır.
# kwargs, fonksiyona bir "dictionary (sözlük)" olarak gelir.

def bilgiler(**kwargs):
    print(kwargs)
    print(type(kwargs))     # <class 'dict'> şeklinde gösterir
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")  # her bir anahtar-değer çiftini yazdırır

bilgiler(ad="Ali", yas=25, sehir="İstanbul")

"""
    ÇIKTI:
    {'ad': 'Ali', 'yas': 25, 'sehir': 'İstanbul'}
    <class 'dict'>
    ad: Ali
    yas: 25
    sehir: İstanbul
"""

"""
    NOT:
    **kwargs, bir fonksiyona istenen sayıda anahtar-değer çifti göndermeyi sağlar.
    Veriler dictionary olarak tutulur → yani anahtar üzerinden erişim mümkündür.
    *args → isimlendirilmemiş veriler (tuple)
    **kwargs → isimlendirilmiş veriler (dict)
"""
