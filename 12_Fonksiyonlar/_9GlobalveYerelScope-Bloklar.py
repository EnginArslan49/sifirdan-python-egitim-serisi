
# Scope = Bir değişkenin nerede tanımlandığı ve nerede kullanılabileceğini belirler.

# --- GLOBAL DEĞİŞKEN ---
# Global değişken: Tüm sayfa tarafından erişilebilir.
x = 10

def ornek():
    # Yerel (local) değişken: Sadece bu fonksiyon içinde geçerli.
    y = 5   # y değişkeni fonksiyon içinde tanımlandığı için bu yerel değişken olur ve y değişkeni yalnızca fonksiyon içinde kullanılabilir
    print("Fonksiyon içinde x:", x)  # Global değişkene erişebilir.
    print("Fonksiyon içinde y:", y)  # Yerel değişkene erişebilir.

ornek()

print("Fonksiyon dışında x:", x)  # Global değişken kullanılabilir.
# print("Fonksiyon dışında y:", y)  # HATA: y sadece fonksiyon içinde tanımlı olduğu için fonksiyonun yerel değişkeni olur ve yalnızca fonksiyon içinde kullanılabilir

# --- GLOBAL DEĞİŞKENİ FONKSİYONDA DEĞİŞTİRME ---
a = 20

def degistir():
    global a  # 'global' anahtar kelimesi global değişkeni değiştirmeye izin verir.
    a = 50

degistir()
print("Yeni global a:", a)  # Artık 50 oldu.

"""
    --- ÖZET ---
    Global değişken → Her yerden erişilebilir.
    Yerel değişken → Sadece tanımlandığı fonksiyon içinde geçerlidir.
"""



# ÖNEMLİ NOKTA: Aynı isimli bir değişken hem global hem local olursa, fonksiyon içinde local olan kullanılır.
# Örnek:

z = 100  # Global değişken

def ornek():
    z = 50  # Local değişken (global z'in üstünü örtmez, sadece fonksiyon içinde geçerli)
    print("Fonksiyon içindeki yerel (local) z değişkeni:", z)

ornek()

print("Fonksiyon dışındaki global z değişkeni:", z)




"""
    Normalde bir fonksiyon içinde bir değişken tanımlarsak, Python onu yerel (local) olarak kabul eder. Ancak 'global' anahtar kelimesi ile bu değişkenin aslında global alandaki (dışarıdaki) değişken olduğunu söyleyebiliriz.
"""

x = 10  # Global değişken

def degistir():
    global x  # Bu satır Python'a "x global değişkendir" der
    x = 20     # Artık global x'in değeri değişir
    print("Fonksiyon içindeki x:", x)

degistir()
print("Fonksiyon dışındaki x:", x)

"""
    ÇIKTI:
    Fonksiyon içindeki x: 20
    Fonksiyon dışındaki x: 20
"""

"""
    --- AÇIKLAMA ---
    'global' kullanılmazsa Python, fonksiyon içindeki x'i yerel (local) sayar.
    'global x' yazarsak artık o değişken dışarıdaki global değişkeni temsil eder.
    Bu sayede fonksiyon içinden global değişkenin değerini değiştirebiliriz.
"""
