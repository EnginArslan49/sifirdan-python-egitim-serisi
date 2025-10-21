
"""
    Sayıları içeren bir dizi oluşturunuz: [10, 20, 30, 40, 50].
    Bu dizideki sayıların ortalamasını hesaplayınız ve ekrana yazdırınız.
"""

sayilar = [10, 20, 30, 40, 50]

toplam = 0

# Dizinin elemanlarının toplamını bulma (ortalama hesaplanırken kullanılacak)
for deger in sayilar:
    toplam += deger

ortalama = toplam / len(sayilar)    # len(sayilar), sayilar listesinin uzunluğunu int cinsinden verir
print(f"Dizinin Ortalaması: {ortalama}")
