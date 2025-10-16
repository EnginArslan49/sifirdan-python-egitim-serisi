
# random modülü, rastgele (random) sayı veya değer üretmek için kullanılır.
# Oyunlar, simülasyonlar, test verisi oluşturma gibi birçok alanda kullanılır.

# Modülün kullanılabilmesi için random kütüphanesinin yüklenmesi gerekmektedir:
import random


# Örnek 1: 0 ile 1 arasında rastgele sayı üretme
sayi = random.random()  # 0.0 ile 1.0 arasında ondalıklı sayı üretir
print("Rastgele sayı:", sayi)


# Örnek 2: Belirli bir aralıkta rastgele tam sayı üretme
tam_sayi = random.randint(1, 10)  # 1 ile 10 dahil arası rastgele tam sayı
print("Rastgele tam sayı:", tam_sayi)


# Örnek 3: Belirli bir aralıktan rastgele sayı (ondalık) üretme
ondalik = random.uniform(10, 20)  # 10.0 ile 20.0 arasında ondalıklı sayı
print("Rastgele ondalıklı sayı:", ondalik)


# Örnek 4: Bir listeden rastgele eleman seçme
renkler = ["kırmızı", "yeşil", "mavi", "sarı"]
secim = random.choice(renkler)
print("Rastgele renk:", secim)


# Örnek 5: Liste elemanlarını karıştırma
sayilar = [1, 2, 3, 4, 5]
random.shuffle(sayilar)  # listeyi karıştırır (in-place değiştirir)
print("Karışık liste:", sayilar)


# Örnek 6: Listeden belirli sayıda rastgele eleman seçme
secimler = random.sample(renkler, 2)  # listedeki 2 farklı elemanı rastgele seçer
print("Rastgele iki renk:", secimler)

"""
    NOT:
    random.random() → 0.0 - 1.0 arası sayı
    random.randint(a, b) → a ile b (dahil) arası tam sayı
    random.choice(liste) → listeden 1 eleman seçer
    random.shuffle(liste) → liste sırasını karıştırır
    random.sample(liste, n) → listeden n farklı eleman seçer
"""
