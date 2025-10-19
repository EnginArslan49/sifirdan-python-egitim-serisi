
"""
    Python'da sınıflarda bir nesne oluşturulduğunda otomatik çalışan özel bir metot vardır. Buna __init__ metodu denir ve genellikle "constructor" olarak adlandırılır.

Amaç:
    - Nesne oluşturulduğunda gerekli başlangıç değerlerini atamak
    - Nesneyi kullanılabilir hale getirmek

Özellikler:
    - Metodun adı __init__ olmalıdır.
    - İlk parametre her zaman self olmalıdır.
    - Nesne oluşturulurken otomatik olarak çalışır.

"""

# Örnek
class Araba:
    def __init__(self, marka, model):
        """
            __init__ metodu: Nesne oluşturulduğunda çalışır.
            self.marka ve self.model ile nesnenin özellikleri belirlenir.
        """
        self.marka = marka  # Kullanıcı Araba metodunda marka alanına parametre olarak ne verirse self.marka ile arabanın markasına eşitlenir
        self.model = model  # Kullanıcı Araba metodunda model alanına parametre olarak ne verirse self.model ile arabanın modeline eşitlenir

    # Arabanın marka ve modelini ekrana yazdırma
    def bilgi(self):
        print(f"Araba: {self.marka} {self.model}")  # Nesnenin davranışı


# Nesne oluşturma
arac1 = Araba("Seat", "Leon")  # __init__ otomatik çalışır
arac1.bilgi()  # Çıktı: Araba: Seat Leon
