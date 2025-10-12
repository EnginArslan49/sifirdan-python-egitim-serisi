
# round() → Sayıları yuvarlamak için kullanılır.
# Kullanım şekli: round(sayi, virgulden-sonra-basamak_sayisi)

# 1. En yakın tam sayıya yuvarlama
x = 10.7
y = round(x)   # 10.7 → 11 olur
print(f"{x} sayısı en yakın tam sayıya yuvarlandı, sonuç: {y}")

# 2. Virgülden sonra belirli basamak bırakma
z = 3.14159
w = round(z, 2)  # 2 basamak bırak → 3.14
print(f"{z} sayısı 2 basamakla yuvarlandı, sonuç: {w}")

# 3. Aşağı veya yukarı otomatik karar verir
# 0.5 ve üstü yukarı, 0.49 ve altı aşağı yuvarlanır
a = 4.5
b = 4.4
print(f"{a} sayısı yuvarlandı, sonuç: {round(a)}")  # 4.5 → 4
print(f"{b} sayısı yuvarlandı, sonuç: {round(b)}")  # 4.4 → 4
