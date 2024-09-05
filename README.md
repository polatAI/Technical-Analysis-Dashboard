# 📊 Teknik Analiz Pano

## 📜 Açıklama

Bu Python tabanlı **Teknik Analiz Pano** uygulaması, hisse senedi verilerini analiz etmek ve görselleştirmek için tasarlanmıştır. **Plotly**, **yfinance**, ve **TA-Lib** kütüphanelerini kullanarak fiyat hareketlerini ve teknik analiz göstergelerini dinamik olarak görselleştirir.

## 🚀 Özellikler

- 📈 **Mum Grafiği**: Hisse senedi fiyat hareketlerinin detaylı bir görünümünü sağlar.
- 🔵 **Basit Hareketli Ortalama (SMA)**: Fiyat hareketlerinin 20 günlük ortalamasını görüntüler.
- 🟢 **Üstel Hareketli Ortalama (EMA)**: Fiyat hareketlerinin 15 günlük üstel ortalamasını hesaplar.
- 📊 **Bollinger Bantları**: Üst, orta ve alt bantlarla fiyat oynaklığını analiz eder.
- 📉 **RSI (Göreceli Güç Endeksi)**: Fiyatın aşırı alım veya aşırı satım koşullarını gösterir.

## 💻 Kurulum

Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:

```bash
pip install plotly yfinance TA-Lib

## 🔧 Kullanımı

1. Projeyi kopyalayın veya indirin.
2. `technical_analysis_dashboard.py` dosyasını açın ve gerekli kütüphaneleri içe aktarın.
3. Uygulamayı şu şekilde çalıştırın:

    ```bash
    python technical_analysis_dashboard.py
    ```

4. Hisse senedi sembolünü ve başlangıç tarihini girin.

## 📝 Örnek Kullanım

```python
if __name__ == "__main__":
    ticker = input("Lütfen hisse senedi sembolünü giriniz: ")
    start_date = input("Lütfen başlangıç tarihini giriniz (YYYY-AA-GG): ")
    dashboard = TechnicalAnalysisDashboard(ticker, start_date)
    dashboard.calculate_indicators()
    dashboard.create_plot()