
# Liste: Birden fazla veriyi tek bir değişkende tutmak için kullanılır.
# Köşeli parantez [] ile tanımlanır.
# Farklı veri tipleri aynı listede bulunabilir (int, string, bool..).

# 1. Liste tanımlama
meyveler = ["elma", "armut", "muz", "çilek"]

# 2. Liste elemanlarını ekrana yazdırma
print(meyveler)

# Listenin belirli elemanlarına ulaşma
ilkEleman = meyveler[0]
print(ilkEleman)

sonEleman = meyveler[len(meyveler)-1] # len(meyveler) ile listenin uzunluğu bulunur ve saymaya 0'dan başlandığı için -1 yazılır
print(sonEleman)