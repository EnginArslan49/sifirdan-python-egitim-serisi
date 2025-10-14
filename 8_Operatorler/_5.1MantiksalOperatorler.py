
# Mantıksal operatörler, birden fazla koşulu (True / False) birleştirip sonuç üretir.
# Genellikle bir sonraki bölümde göreceğimiz if-else koşul blokları yapılarında karar vermek için kullanılır.

# Operatörler:
# and → ve
# or  → veya
# not → değil

a = 10
b = 5
c = 2

# --------------------------
# AND (ve)
# Tüm koşullar True ise sonuç True olur.
#   True, True => True
#   False, True => False
#   False, False => False

print( a > b and (b > c) )   # True, çünkü her iki ifade de doğru
print( a > b and b < c )   # False, çünkü ikinci koşul yanlış



# --------------------------
# OR (veya)
# Koşullardan en az biri True ise sonuç True olur.
#   True, True => True
#   False, True => True
#   False, False => False

print( a > b or b < c )    # True, çünkü ilk koşul doğru
print( a < b or b < c )    # False, çünkü her iki koşul da yanlış



# --------------------------
# NOT (değil)
# Koşulun tersini alır (True ↔ False)
#   True => False
#   False => True

print( not (a > b) )       # False, çünkü a > b ifadesi True’dur
print( not (b < c) )       # True, çünkü b < c ifadesi False’dur