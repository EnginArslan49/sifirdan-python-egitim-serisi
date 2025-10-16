

# 1. int() → Tam sayıya çevirme
sayi_float = 10.99
# sayi_float tipi float iken int() ile tam sayıya dönüştürdük
sayi_int = int(sayi_float)   # 10
print(sayi_int)


sayi_str = "25"
# sayi_str tipi str iken int() ile tam sayıya dönüştürdük
sayi_int2 = int(sayi_str)    # 25
print(sayi_int2)


# 2. float() → Ondalıklı sayıya çevirme
sayi = 10
# sayi tipi int iken float() ile ondalıklı sayıya dönüştürdük
sayi_float = float(sayi)     # 10.0
print(sayi_float)

sayi_str2 = "19.99"
# sayi_str2 tipi str iken float() ile ondalıklı sayıya dönüştürdük
sayi_float2 = float(sayi_str2) # 19.99
print(sayi_float2)


# 3. str() → Metne çevirme
sayi = 25
# sayi tipi int iken str() ile metne dönüştürdük
sayi_str3 = str(sayi)        # "25"
print(sayi_str3)

aktif = True
# aktif tipi bool iken str() ile metne dönüştürdük
aktif_str = str(aktif)       # "True"
print(aktif_str)


# 4. bool() → Mantıksal değere çevirme
x = 0
# x tipi int iken bool() ile mantıksal değere dönüştürdük (0 → False)
print(bool(x))   # False

y = 10
# y tipi int iken bool() ile mantıksal değere dönüştürdük (0 dışı → True)
print(bool(y))  # True


# ==============================
#           Özet:
#       int() → tam sayı
#       float() → ondalıklı sayı
#       str() → metin
#       bool() → doğru/yanlış veya 1/0
# ==============================
