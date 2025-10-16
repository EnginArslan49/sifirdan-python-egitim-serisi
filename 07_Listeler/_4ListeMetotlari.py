
# LISTE METOTLARI - ÖRNEK KODLAR

# Örnek liste oluşturma
programlama_diller = ["Python", "C#", "Java", "Javascript", "Python", "C++"]
print("Orijinal liste:", programlama_diller)
# Çıktı: Orijinal liste: ['Python', 'C#', 'Java', 'Javascript', 'Python', 'C++']

# 1. append() - Listenin sonuna eleman ekler
programlama_diller.append("Go")
print("append('Go') sonrası:", programlama_diller)
# Çıktı: append('Go') sonrası: ['Python', 'C#', 'Java', 'Javascript', 'Python', 'C++', 'Go']

# 2. clear() - Listedeki tüm elemanları siler
kopya_liste = programlama_diller.copy()
kopya_liste.clear()
print("clear() sonrası:", kopya_liste)
# Çıktı: clear() sonrası: []

# 3. count() - Bir değerin listedeki tekrar sayısını döndürür
python_sayisi = programlama_diller.count("Python")
print("count('Python') sonucu:", python_sayisi)
# Çıktı: count('Python') sonucu: 2

# 4. index() - Aranan değerin listedeki ilk index numarasını döndürür
java_index = programlama_diller.index("Java")
print("index('Java') sonucu:", java_index)
# Çıktı: index('Java') sonucu: 2

# 5. insert() - Belirtilen indeks konumuna eleman ekler
programlama_diller.insert(1, "Ruby") # 2. elemnana Ruby değerini ekler
print("insert(1, 'Ruby') sonrası:", programlama_diller)
# Çıktı: insert(1, 'Ruby') sonrası: ['Python', 'Ruby', 'C#', 'Java', 'Javascript', 'Python', 'C++', 'Go']

# 6. pop() - Belirtilen indeksteki elemanı siler (varsayılan: son eleman)
silinen_eleman = programlama_diller.pop()
print(f"pop() sonrası - Silinen: {silinen_eleman}, Liste: {programlama_diller}")
# Çıktı: pop() sonrası - Silinen: Go, Liste: ['Python', 'Ruby', 'C#', 'Java', 'Javascript', 'Python', 'C++']

silinen_eleman2 = programlama_diller.pop(2)
print(f"pop(2) sonrası - Silinen: {silinen_eleman2}, Liste: {programlama_diller}")
# Çıktı: pop(2) sonrası - Silinen: C#, Liste: ['Python', 'Ruby', 'Java', 'Javascript', 'Python', 'C++']

# 7. remove() - Belirtilen değeri listeden siler (ilk bulduğunu siler)
programlama_diller.remove("Python")
print("remove('Python') sonrası:", programlama_diller)
# Çıktı: remove('Python') sonrası: ['Ruby', 'Java', 'Javascript', 'Python', 'C++']

# 8. reverse() - Liste elemanlarını tersten sıralar
programlama_diller.reverse()
print("reverse() sonrası:", programlama_diller)
# Çıktı: reverse() sonrası: ['C++', 'Python', 'Javascript', 'Java', 'Ruby']

# 9. sort() - Listedeki elemanları sayısal ya da alfabetik olarak sıralar
programlama_diller.sort()
print("sort() sonrası:", programlama_diller)
# Çıktı: sort() sonrası: ['C++', 'Java', 'Javascript', 'Python', 'Ruby']

# SAYISAL LİSTE ÖRNEĞİ
sayilar = [5, 2, 8, 1, 9, 3]
print("\nSayılar listesi:", sayilar)
# Çıktı: Sayılar listesi: [5, 2, 8, 1, 9, 3]

sayilar.sort()
print("Küçükten büyüğe sort():", sayilar)
# Çıktı: Küçükten büyüğe sort(): [1, 2, 3, 5, 8, 9]

sayilar.sort(reverse=True)
print("Büyükten küçüğe sort(reverse=True):", sayilar)
# Çıktı: Büyükten küçüğe sort(reverse=True): [9, 8, 5, 3, 2, 1]

# 10. min() - Listedeki elemanların sayısal veya alfabetik olarak (her ikisindede çalışır) en küçüğünü verir
sayi = [54, 45, 2, 3]
print( min(sayi) ) # Çıktı: 2

# 10. max() - Listedeki elemanların sayısal veya alfabetik olarak (her ikisindede çalışır) en büyüğünü verir
sayi = [54, 45, 2, 3]
print( max(sayi) ) # Çıktı: 54

# EK METOTLAR
# copy() - listenin kopyasını oluşturur
kopya = programlama_diller.copy()
print("\ncopy() ile kopya liste:", kopya)
# Çıktı: copy() ile kopya liste: ['C++', 'Java', 'Javascript', 'Python', 'Ruby']

# extend() - başka bir listeyi mevcut listeye ekler
yeni_diller = ["Swift", "Kotlin"]
programlama_diller.extend(yeni_diller)
print("extend() sonrası:", programlama_diller)
# Çıktı: extend() sonrası: ['C++', 'Java', 'Javascript', 'Python', 'Ruby', 'Swift', 'Kotlin']

