
# Liste tanımlama
programlama_diller = ["Python","C#","Java","Javascript"]

# Liste atama
sonuc = programlama_diller
# Çıktı: ['Python', 'C#', 'Java', 'Javascript']

# Liste tipini öğrenme
sonuc = type(programlama_diller)
# Çıktı: <class 'list'>

# Liste dilimleme - 0. indeksten 2. indekse kadar (2 dahil değil)
sonuc = programlama_diller[0:2]
# Çıktı: ['Python', 'C#']

# Liste dilimleme - başlangıçtan 2. indekse kadar
sonuc = programlama_diller[:2]
# Çıktı: ['Python', 'C#']

# Liste dilimleme - tüm liste
sonuc = programlama_diller[:] # veya sonuc = programlama_diller
# Çıktı: ['Python', 'C#', 'Java', 'Javascript']

# Liste dilimleme - negatif indekslerle (-3'ten -1'e kadar) (-1 "son eleman" dahil değil)
sonuc = programlama_diller[-3:-1]
# Çıktı: ['C#', 'Java']

# Liste dilimleme - negatif indekslerle (-3'ten sona kadar)
sonuc = programlama_diller[-3:]
# Çıktı: ['C#', 'Java', 'Javascript']


# Güncelleme - son elemanı değiştirme
programlama_diller[-1] = "Php"
# Liste artık: ['Python', 'C#', 'Java', 'Php']

# Güncellenmiş listeyi görüntüleme
sonuc = programlama_diller
# Çıktı: ['Python', 'C#', 'Java', 'Php']


# Liste uzunluğu
sonuc = len(programlama_diller)
# Çıktı: 4

# Liste birleştirme
sonuc = programlama_diller + ["Go","Delphi"]
# Çıktı: ['Python', 'C#', 'Java', 'Php', 'Go', 'Delphi']

print(sonuc)
# Son çıktı: ['Python', 'C#', 'Java', 'Php', 'Go', 'Delphi']


# Eleman Silme (del komutu ile)
iller = ["Ağrı", "Muş", "Bitlis"]
del iller[0] # iller listesi içinden 0. (ilk) eleman del komutuyla silinir
print(iller)
# Çıktı: ["Muş", "Bitlis"]

# Eleman Silme (remove komutu ile)
iller.remove("Muş") # remove komutu kendisine verilen parametreyi liste içinden siler (Verilen parametre liste içinde yoksa hata verir)
print(iller)
# Çıktı: ["Bitlis"]


# Bir elemanı liste içinde varmı diye kontrol ettirme
ilceler = ["Ahlat", "Adilcevaz", "Mutki"]

esenlerVarMi = "Esenler" in ilceler
print(hakYemisVarMi)