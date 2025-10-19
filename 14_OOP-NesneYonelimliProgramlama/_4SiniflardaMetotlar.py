
"""
    Metotlar, bir sınıfa ait işlevlerdir. Yani nesnenin "yapabildiği işlerdir".
    Fonksiyon gibi çalışırlar ama sınıfın içinde tanımlanırlar ve o sınıfa ait nesneler tarafından kullanılırlar.

Özellikler:
    - Sınıfın davranışlarını temsil eder.
    - İlk parametre olarak her zaman self alır.
    - Nesneye özel verilere erişebilir.

"""

# Örnek:
class Araba:
    # self: oluşturulan nesnenin kendisi
    # marka ve model: nesneye ait veriler
    def __init__(self, marka, model):   # Bu metot nesne oluşturulurken otomatik çalışır
        self.marka = marka
        self.model = model

    # Bu metot araba sınıfının özelliklerini ekrana yazdırır.
    def bilgi(self):
        print(f"Araba: {self.marka} {self.model}")

    # Bu metot araba sınıfının özelliklerinden olan markayı değiştirir
    def degistir_marka(self, yeni_marka):
        self.marka = yeni_marka

# Nesne oluşturma
arac1 = Araba("Toyota", "Corolla")

# Metotları kullanma
arac1.bilgi()            # Çıktı: Araba: Toyota Corolla
arac1.degistir_marka("Honda")
arac1.bilgi()            # Çıktı: Araba: Honda Corolla
