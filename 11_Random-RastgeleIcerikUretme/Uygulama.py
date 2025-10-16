
"""
    UYGULAMA:
    Yazı - tura uygulamasını random modülünü kullanarak yapınız (Random kütüphanesini eklemeyi unutmayın)
"""

import random   # Random kütüphanesi
from operator import ifloordiv

# YÖNTEM 1: LİSTE KULLANARAK
secenekler = ["Yazı", "Tura"]

secilen = random.sample(secenekler, 1)  # secenekler listesinden rastgele bir değer seç

print(secilen)




# YÖNTEM 2: İNT DEĞER KULLANARAK

yaziTuraDegeri = random.randint(1, 2)   # 1 ile 2 arasında rastgele bir sayı seç

if yaziTuraDegeri == 1:
    print("Yazı")

else:
    print("Tura")




# YÖNTEM 3: FONKSİYON KULLANARAK
def yaziTuraAt():
    deger = random.randint(1, 2)   # 1 ile 2 arasında rastgele bir sayı seç
    return deger

sonuc = ""
if yaziTuraAt() == 1:
    sonuc = "Yazı"

else:
    sonuc = "Tura"

print( sonuc )
