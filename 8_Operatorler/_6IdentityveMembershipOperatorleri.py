
# IDENTITY OPERATÖRLERİ (is, is not)
# Aynı nesne mi kontrol eder

# is operatörü
liste1 = ["python", "java"]
liste2 = liste1  # aynı referans
liste3 = ["python", "java"]  # farklı referans

print("liste1 ve liste2 aynı nesne mi:", liste1 is liste2)  # True
print("liste1 ve liste3 aynı nesne mi:", liste1 is liste3)  # False

# is not operatörü
print("liste1 ve liste3 farklı nesne mi:", liste1 is not liste3)  # True

# None kontrolü
bos_deger = None
print("bos_deger None mı:", bos_deger is None)  # True

# MEMBERSHIP OPERATÖRLERİ (in, not in)
# İçinde var mı kontrol eder

diller = ["python", "java", "c++"]
isim = "Mehmet"

# in operatörü
print("python listede var mı:", "python" in diller)  # True
print("m harfi isimde var mı:", "m" in isim)  # True

# not in operatörü
print("javascript listede yok mu:", "javascript" not in diller)  # True
print("z harfi isimde yok mu:", "z" not in isim)  # True

# Sözlük üzerinde kontrol
kisi = {"ad": "Ali", "yas": 25}
print("ad anahtarı sözlükte var mı:", "ad" in kisi)  # True
print("soyad anahtarı sözlükte yok mu:", "soyad" not in kisi)  # True