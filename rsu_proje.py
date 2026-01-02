import time
import math

class BenimRSU:
    def __init__(self, seed=None):
        if seed is None:
            # Seed girilmezse zamanı kullan (Tamamen rastgelelik için)
            self.state = int(time.time())
        else:
            self.state = seed
        
        # LCG Algoritması Parametreleri (Örnek değerler)
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def rastgele_sayi_uret(self):
        # Formül: Key = G(seed)
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def rastgele_bit_dizisi_uret(self, uzunluk=1000):
        bit_dizisi = ""
        while len(bit_dizisi) < uzunluk:
            sayi = self.rastgele_sayi_uret()
            # Sayıyı binary'ye çevir ve ekle
            bit_dizisi += format(sayi, 'b')
        return bit_dizisi[:uzunluk]

# --- TEST KISMI ---
def istatistiksel_testler(bit_dizisi):
    print(f"Üretilen Dizi (İlk 50 bit): {bit_dizisi[:50]}...")
    
    # 1. Kriter: 0 ve 1 Eşitliği (Frequency Test)
    birler = bit_dizisi.count('1')
    sifirlar = bit_dizisi.count('0')
    toplam = len(bit_dizisi)
    
    print("\n--- 1. Test: 0-1 Eşitliği ---")
    print(f"1 Sayısı: {birler} (%{birler/toplam*100:.2f})")
    print(f"0 Sayısı: {sifirlar} (%{sifirlar/toplam*100:.2f})")
    
    if 0.45 < (birler/toplam) < 0.55:
        print("SONUÇ: BAŞARILI (Denge var)")
    else:
        print("SONUÇ: BAŞARISIZ (Denge yok)")

    # 2. Kriter: Ki-Kare Testi (Chi-Square)
    # Beklenen dağılım %50 0, %50 1 olmalı.
    beklenen = toplam / 2
    chi_square = ((sifirlar - beklenen)**2 / beklenen) + ((birler - beklenen)**2 / beklenen)
    
    print("\n--- 2. Test: Ki-Kare (Chi-Square) ---")
    print(f"Ki-Kare Değeri: {chi_square}")
    # Serbestlik derecesi 1 ve %5 anlamlılık düzeyi için kritik değer 3.841'dir.
    if chi_square < 3.841:
        print("SONUÇ: BAŞARILI (Rastgele dağılıma uygun)")
    else:
        print("SONUÇ: BAŞARISIZ (Rastgelelik şüpheli)")

# Çalıştırma
rsu = BenimRSU(seed=12345) # İstersen seed'i boş bırak
uretilen_data = rsu.rastgele_bit_dizisi_uret(uzunluk=10000)
istatistiksel_testler(uretilen_data)