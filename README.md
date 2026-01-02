# LCG Tabanlı Rastgele Sayı Üreteci (RSÜ) 🛡️

Bu proje, kriptografik anahtar üretimi için gerekli olan iki temel kriteri (**rastgelelik** ve **istatistiksel kalite**) karşılamak amacıyla geliştirilmiş bir **Rastgele Sayı Üreteci (RSÜ)** uygulamasıdır.

## 📋 Proje Hakkında
Kriptografi dünyasında güvenli bir anahtarın tahmin edilemez olması şarttır. Bu çalışmada, geniş çapta kabul gören ve verimli çalışan **Linear Congruential Generator (LCG)** algoritması kullanılarak 0-1 bit dizileri üretilmiştir.

### ⚙️ Algoritma Mantığı
Üretici, bir "seed" (tohum) değerini girdi olarak alır ve aşağıdaki matematiksel fonksiyonu ($G$) kullanarak bir sonraki değeri hesaplar:

$$Key = (a \cdot Seed + c) \pmod{m}$$

* **Seed:** Başlangıç değeri (zaman damgası veya kullanıcı girdisi).
* **a (Multiplier):** Çarpan sabiti.
* **c (Increment):** Artış sabiti.
* **m (Modulus):** Mod değeri (Üretilen sayıların aralığını belirler).

---

## 📊 İstatistiksel Kalite ve Testler
Algoritmanın bir anahtar olarak kullanılabilirliğini kanıtlamak için iki ana test uygulanmıştır:

| Test Adı | Açıklama | Beklenen Sonuç |
| :--- | :--- | :--- |
| **Frekans Testi** | Üretilen 0 ve 1 bitlerinin sayıca birbirine yakınlığını ölçer. | %50 - %50 Denge |
| **Ki-Kare Testi** | Verilerin rastgelelikten sapma oranını istatistiksel olarak hesaplar. | $\chi^2 < 3.841$ (Başarılı) |

> **Not:** Yapılan testlerde algoritmamız kritik değer olan 3.841'in altında kalarak istatistiksel olarak "rastgele" kabul edilmiştir.

---

## 📂 Depo İçeriği
Hocamızın istediği tüm materyaller aşağıda listelenmiştir:
* `rsu_proje.py`: Algoritmanın kaynak kodu.
* `akis_semasi.png`: Algoritmanın mantıksal işleyiş şeması.
* `sozde_kod.txt`: Algoritmanın adım adım açıklaması (Pseudo-code).
* `test_sonuclari.txt`: Kodun ürettiği çıktıların ve testlerin raporu.

---

## 🚀 Nasıl Çalıştırılır?
Projenin çıktılarını gözlemlemek için Python yüklü bir terminalde şu komutu çalıştırmanız yeterlidir:
```bash
python rsu_proje.py
