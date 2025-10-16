
"""
    UYGULAMA 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayın
    Alan Bulma Formülü: πr²
    Çevre Bulma Formülü: 2πr
"""

# NOT: π (pi)'yi 3.14 olarak alınız

# ÇÖZÜM

yariCap = float(input("Yarıçap? : "))
PI = 3.14

alan = PI * (yariCap * yariCap) # Alan Hesaplama
cevre = 2 * PI * yariCap  # Çevre Hesaplama

print("Alan: " + str(alan))
print("Çevre: " + str(cevre))