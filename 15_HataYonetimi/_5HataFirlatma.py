
"""
    Bazı durumlarda hatayı Python’un kendisinin yakalamasını beklemek yerine, biz kendimiz bilinçli olarak hata oluşturmak isteyebiliriz. Buna “hata fırlatma” (raise) denir.

    Amaç:
     - Belirli bir koşul gerçekleştiğinde programın akışını durdurmak,
     - Kullanıcıyı veya geliştiriciyi yanlış duruma karşı uyarmak,
     - Hatanın nedenini açıkça belirtmek için kullanılır.

        # `raise` anahtar kelimesi ile yapılır.
"""
from sys import exception


# Örnek 1:
def yas_kontrol(yas):
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")  # Hata oluşturuluyor
    else:
        print("Yaş geçerli.")

try:
    yas_kontrol(-5)
except Exception as hata:
    print("Hata yakalandı:", hata)
"""
    EXCEPT 2:
        except ValueError as hata:
        print("Hata yakalandı:", hata)
"""



# Örnek 2: Koşula göre farklı hata türü fırlatma
def bolme(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölme hatası!")  # Özel hata mesajı "ZeroDivisionError: (2. sayının 0olma Durumu)"
    return a / b

try:
    sonuc = bolme(10, 0)
    print(sonuc)
except ZeroDivisionError as hata:
    print("Hata yakalandı:", hata)

"""
    Özet:
     - raise → Hata oluşturur.
     - Hata türü (ValueError, TypeError, vb.) programcının seçimine bağlıdır.
     - Bu yöntem, kontrollü ve güvenli kod yazmak için önemlidir.
"""
