
# Operatörler, değişkenler ve değerler üzerinde işlem yapmamızı sağlar.
# Örneğin toplama, karşılaştırma veya mantıksal işlemler gibi.

# Operatör türleri:
# 1. Aritmetik Operatörler
# 2. Karşılaştırma Operatörleri
# 3. Mantıksal Operatörler
# 4. Atama Operatörleri
# 5. Üyelik Operatörleri
# 6. Kimlik (Identity) Operatörleri

# Her biri farklı amaçlarla kullanılır.
# Aşağıda her tür için 2 basit örnek göreceğiz.

# --------------------------------
# 1. Aritmetik Operatörler
# (+, -, *, /, //, %, **)
x = 10
y = 3
print("Toplama:", x + y)   # 13
print("Üs alma:", x ** y)  # 1000

# --------------------------------
# 2. Karşılaştırma Operatörleri
# (==, !=, >, <, >=, <=)
a = 5
b = 8
print(a == b)   # False, çünkü 5 eşit değil 8’e
print(a < b)    # True, çünkü 5 küçüktür 8’den

# --------------------------------
# 3. Mantıksal Operatörler
# (and, or, not)
print(True and False)  # False, çünkü her iki taraf True olmalı
print(not True)        # False, çünkü not tersini alır

# --------------------------------
# 4. Atama Operatörleri
# (=, +=, -=, *=, /=, ...)
z = 5
z += 3   # z = z + 3 → 8
z *= 2   # z = z * 2 → 16
print(z) # 16

# --------------------------------
# 5. Üyelik Operatörleri
# (in, not in)
liste = [1, 2, 3, 4]
print(3 in liste)      # True, çünkü 3 listede var
print(5 not in liste)  # True, çünkü 5 listede yok

# --------------------------------
# 6. Kimlik (Identity) Operatörleri
# (is, is not)
a = [1, 2]
b = [1, 2]
c = a
print(a is b)      # False, çünkü farklı nesneler
print(a is c)      # True, çünkü aynı nesneye işaret ediyor
