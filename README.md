# Jigsaw Görüntü Oluşturma Projesi

Bu proje, Python kullanarak çeşitli görsel manipülasyon ve oluşturma tekniklerini gösteren bir koleksiyondur. Proje üç ana bileşenden oluşmaktadır:

## 📁 Proje İçeriği

### 1. `jigsaw.py` - Puzzle Görüntü Oluşturucu
Bu script, bir görseli parçalara ayırıp karıştırarak puzzle benzeri görüntüler oluşturur.

**Özellikler:**
- Görseli 3x3 ve 4x4 grid boyutlarında parçalara ayırma
- Her grid boyutu için 3 farklı karışık versiyon oluşturma
- Orijinal ve karışık versiyonları yan yana görselleştirme
- 256x256 piksel boyutunda kare görsel işleme

**Kullanılan Kütüphaneler:**
- `numpy` - Dizi işlemleri
- `matplotlib.pyplot` - Görselleştirme
- `PIL` - Görsel işleme
- `random` - Rastgele karıştırma

### 2. `rgb1.py` - Sinüs/Kosinüs Tabanlı RGB Görsel Oluşturucu
Bu script, matematiksel fonksiyonlar kullanarak renkli görsel oluşturur.

**Özellikler:**
- 500x500 piksel boyutunda görsel
- R, G, B kanalları için farklı trigonometrik fonksiyonlar
- Sinüs ve kosinüs kombinasyonları ile renk geçişleri
- 0-1 aralığında normalize edilmiş renk değerleri

**Matematiksel Formüller:**
- **R Kanalı:** `(1 + sin(X + Y)) / 2`
- **G Kanalı:** `(1 + cos(X - Y)) / 2`
- **B Kanalı:** `(1 + sin(X) * cos(Y)) / 2`

### 3. `rgb2.py` - 3D R Kanalı Görselleştirici
Bu script, R kanalının 3 boyutlu yüzey grafiğini oluşturur.

**Özellikler:**
- 256x256 piksel çözünürlük
- 3D yüzey grafiği
- 8-bit renk değerleri (0-255 arası)
- Plasma renk haritası kullanımı

**Matematiksel Formül:**
- **R Kanalı:** `128 + 127 * sin(2πx)`

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
```bash
pip install numpy matplotlib pillow
```

### Çalıştırma
Her script'i ayrı ayrı çalıştırabilirsiniz:

```bash
python jigsaw.py
python rgb1.py
python rgb2.py
```

## 📋 Kullanım Notları

### jigsaw.py için:
- `IMAGE_PATH` değişkenini kendi görsel dosyanızın yolu ile değiştirin
- Görsel otomatik olarak 256x256 piksel boyutuna yeniden boyutlandırılır
- Sonuçlar matplotlib penceresinde gösterilir

### rgb1.py için:
- Görsel boyutu `size` değişkeni ile ayarlanabilir
- Renk kanalları matematiksel formüller ile hesaplanır
- Sonuç doğrudan görselleştirilir

### rgb2.py için:
- 3D görselleştirme için `mpl_toolkits.mplot3d` kullanılır
- Yüzey grafiği interaktif olarak görüntülenebilir
- Renk haritası `plasma` olarak ayarlanmıştır

## 🎯 Proje Amaçları

1. **Görsel İşleme:** Farklı görsel manipülasyon tekniklerini gösterme
2. **Matematiksel Görselleştirme:** Trigonometrik fonksiyonlar ile renk oluşturma
3. **3D Görselleştirme:** Renk kanallarının 3 boyutlu analizi
4. **Puzzle Oluşturma:** Görselleri parçalara ayırıp karıştırma

## 🔧 Teknik Detaylar

- **Dil:** Python 3.x
- **Ana Kütüphaneler:** NumPy, Matplotlib, PIL
- **Görsel Formatları:** RGB, PNG
- **Koordinat Sistemi:** Cartesian (x, y)

## 📝 Lisans

Bu proje eğitim amaçlı oluşturulmuştur. Kodlar açık kaynak olarak paylaşılmaktadır.
