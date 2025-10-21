
"""
    1’den 100’e kadar olan sayılar arasında 3 ve 5’e tam bölünen sayıları ekrana yazdırınız.
"""

# YÖNTEM 1
print("1’den 100’e kadar olan sayılar arasında 3 ve 5’e tam bölünen sayılar: ")

for sayi in range(1, 101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print(sayi)




# YÖNTEM 2 => Liste Kullanarak
tamBolunenSayilar = []

for sayi in range(1, 101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        tamBolunenSayilar.append(sayi)

print(f"1’den 100’e kadar olan sayılar arasında 3 ve 5’e tam bölünen sayılar: {tamBolunenSayilar}")
