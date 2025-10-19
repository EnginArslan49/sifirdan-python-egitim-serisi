
"""
    Hata ayıklama (debugging), bir programda oluşan hataları (bug) bulma, nedenini anlama ve düzeltme sürecidir.

    Amaç:
     - Programın beklenmedik şekilde davranmasının nedenini bulmak
     - Hatalı kodu tespit edip düzeltmek
     - Programın doğru ve kararlı çalışmasını sağlamak

    Yöntemler:
     - print() ile değişken değerlerini adım adım izlemek
     - try–except blokları ile hata noktalarını yakalamak
     - IDE araçlarını (örneğin PyCharm Debugger) kullanarak kodu adım adım çalıştırmak
     - Loglama (logging) kullanarak hata kayıtlarını incelemek
"""

# Örnek:
def bolme(a, b):
    try:
        sonuc = a / b
        return sonuc
    except ZeroDivisionError:
        return "Hata: Sıfıra bölme yapılamaz."
    except Exception as e:
        print("Beklenmeyen hata:", e)

print(bolme(10, 2))   # Normal çalışır (5.0)
print(bolme(10, 0))   # Hata yakalanır (Hata: Sıfıra bölme yapılamaz.)

"""
    Özet:
     - Debugging = Hata bulma ve düzeltme süreci
     - Hataları anlamak, izlemek ve gidermek için kullanılır
     - En etkili yöntem: adım adım izleme + logging + exception yönetimi
"""
