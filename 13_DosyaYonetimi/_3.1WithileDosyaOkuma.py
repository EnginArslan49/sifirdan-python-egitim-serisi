
"""
    'with' yapısı, dosyayı otomatik olarak açar ve iş bittikten sonra kapatır.
    Bu sayede 'close()' metodunu yazmaya gerek kalmaz.
    Bu yöntem güvenlidir, dosya sızıntısı (memory leak) riskini önler.
"""

# Örnek dosya okuma işlemi
with open("_3.2log.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir, end="")  # end="" yazınca fazladan boş satır bırakmaz

"""
    AÇIKLAMA:
    - "r" → okuma modudur. Dosya yoksa hata verir.
    - encoding="utf-8" → Türkçe karakterlerin doğru görüntülenmesi için kullanılır.
    - 'with' bloğu bittiğinde dosya otomatik olarak kapanır.
"""
