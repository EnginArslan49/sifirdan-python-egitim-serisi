
"""
    Class (Sınıf), bir nesnenin taslağıdır.  Yani, nesnenin sahip olacağı özellikleri ve yapabileceği işleri  önceden tanımlayan şablondur.
"""

# Örnek sınıf tanımı
class Araba:
    def __init__(self, marka, model):
        self.marka = marka  # Özellik (attribute)
        self.model = model  # Özellik (attribute)

    def bilgi(self):
        print(f"Araba: {self.marka} {self.model}")  # Metot (davranış)

"""
Object (Nesne), bir sınıftan üretilmiş somut örnektir. Sınıfın tanımladığı özelliklere ve davranışlara sahiptir.
"""
# Sınıftan nesne oluşturma
arac1 = Araba("Toyota", "Corolla")  # arac1 nesnesi Araba sınıfının örneği
arac1.bilgi()  # Çıktı: Araba: Toyota Corolla
