
# Set (küme), benzersiz elemanlardan oluşan, sırasız (unordered) bir koleksiyondur.
# Aynı eleman birden fazla kez bulunamaz.
# Süslü parantez {} ile tanımlanır.
# Yalnızca eleman eklenebilir veya silinebilir.

# ÖNEMLİ NOT: set listeler içinde birbirinden farklı birden fazla veri tipli değişkenler (int, string, bool..) tanımlanabilir.

# 1. Set tanımlama
sayilar = {1, 2, 3, 4, 5, 5, 2}  # Tekrar eden elemanlar otomatik silinir
print("Küme:", sayilar)  # Çıktı: {1, 2, 3, 4, 5}

# 2. Eleman ekleme
sayilar.add(6)
print("6 eklendikten sonra:", sayilar)

# 3. Birden fazla eleman ekleme
sayilar.update([7, 8, 9])
print("Yeni elemanlar eklendi:", sayilar)

# 4. Eleman silme
sayilar.remove(3)  # 3 varsa siler, yoksa hata verir
print("3 silindikten sonra:", sayilar)

# 5. discard() → Elemanı siler, yoksa hata vermez
sayilar.discard(10)  # 10 yok ama hata oluşmaz
print("discard(10) sonrası:", sayilar)

# 6. pop() → Rastgele bir elemanı siler
silinen = sayilar.pop()
print("Silinen eleman:", silinen)
print("pop ile eleman silme sonrası küme:", sayilar)

# 7. clear() → Tüm elemanları siler
sayilar.clear()
print("clear() sonrası boş küme:", sayilar)