
"""
    Kullanıcıdan bir sayı alınız ve bu sayının mükemmel sayı olup olmadığını kontrol ediniz.
    Mükemmel sayı, kendisi hariç pozitif bölenlerinin toplamı kendisine eşit olan sayıdır. (Örneğin: 6, 28)
"""

alinanSayi = int(input("Bir sayı giriniz: "))

toplam = 0
for i in range(1, alinanSayi):
    if alinanSayi % i == 0:
        toplam += i


if toplam != alinanSayi:
    print(f"Girilen {alinanSayi} sayısı mükemmel sayı değildir!")
else:
    print(f"Girilen {alinanSayi} sayısı mükemmel sayıdır!")
