
# Atama operatörleri, bir değişkene değer atamak veya mevcut değeri güncellemek için kullanılır.
# Örneğin: a = 5 ifadesi, 'a' değişkenine 5 değerini atar.

a = 10  # Başlangıç değeri

# =   → Eşittir (değer atama)
a = 5
print("=  Sonuç:", a)   # 5

# +=  → Arttırma eşit (a = a + 5)
a += 5
print("+= Sonuç:", a)   # 10

# -=  → Eksiltme eşit (a = a - 3)
a -= 3
print("-= Sonuç:", a)   # 7

# *=  → Çarpım eşit (a = a * 2)
a *= 2
print("*= Sonuç:", a)   # 14

# /=  → Bölme eşit (a = a / 2)
a /= 2
print("/= Sonuç:", a)   # 7.0

# %=  → Mod eşit (a = a % 4)
a %= 4
print("%= Sonuç:", a)   # 3.0 (7 mod 4 = 3)

# //= → Tam bölen eşit (a = a // 2)
a //= 2
print("//= Sonuç:", a)  # 1.0 (3 // 2 = 1)

# **= → Üs alma eşit (a = a ** 3)
a **= 3
print("**= Sonuç:", a)  # 1.0 (1 üzeri 3 = 1)
