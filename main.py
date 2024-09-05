import plotly.graph_objs as go
import yfinance as yf
import talib as ta
import plotly.io as pio
from plotly.subplots import make_subplots
from datetime import datetime

# Plotly render seçeneğini tarayıcıda görüntülemek için ayarlıyoruz
pio.renderers.default = "browser"

class TechnicalAnalysisDashboard:
    def __init__(self, ticker, start_date):
        """
        Sınıfın başlatıcı metodudur. Hisse senedi sembolü ve başlangıç tarihi alır.
        Ayrıca, mevcut tarihi alır ve veri indirme işlemini başlatır.
        """
        self.ticker = ticker  # Kullanıcıdan alınan hisse senedi sembolü
        self.start_date = start_date  # Kullanıcıdan alınan başlangıç tarihi
        self.end_date = datetime.now().strftime('%Y-%m-%d')  # Mevcut tarihi alır
        self.df = self.download_data()  # Veriyi indirir ve saklar
        
    def download_data(self):
        """
        Belirtilen tarih aralığında ve hisse senedi sembolü için verileri indirir.
        4 saatlik zaman diliminde veri indirir.
        Eğer veri bulunamazsa, kullanıcıyı bilgilendirir ve None döndürür.
        """
        df = yf.download(self.ticker, start=self.start_date, end=self.end_date, interval='1d')
        if df.empty:
            print("No data found for the given date range and ticker symbol.")
            return None
        return df
    
    def calculate_indicators(self):
        """
        Teknik analiz göstergelerini hesaplar: SMA, EMA, RSI ve Bollinger Bantları.
        Hesaplanan göstergeler veri çerçevesine eklenir.
        """
        if self.df is not None:
            # Basit Hareketli Ortalama (SMA) hesaplama
            self.df['SMA'] = ta.SMA(self.df['Close'], timeperiod=20)
            # Üssel Hareketli Ortalama (EMA) hesaplama
            self.df['EMA'] = ta.EMA(self.df['Close'], timeperiod=15)
            # Göreceli Güç Endeksi (RSI) hesaplama
            self.df['RSI'] = ta.RSI(self.df['Close'], timeperiod=14)
            # Bollinger Bantları hesaplama
            self.df['Upper_BB'], self.df['Middle_BB'], self.df['Lower_BB'] = ta.BBANDS(
                self.df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0
            )
    
    def create_plot(self):
        """
        Teknik analiz grafiğini oluşturur ve görselleştirir.
        İki alt grafikte (subplot) gösterim sağlar: biri fiyat ve göstergeler, diğeri RSI.
        """
        if self.df is None:
            return
        
        # Grafik düzenlemelerini oluşturuyoruz
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            vertical_spacing=0.3, row_heights=[0.7, 0.3],
                            subplot_titles=[f'{self.ticker} Price and Indicators', 'RSI'])

        # Mum grafiği (candlestick) oluşturuyoruz
        candlestick = go.Candlestick(
            x= self.df.index ,
            open=self.df.Open,
            high=self.df.High,
            low=self.df.Low,
            close=self.df.Close,
            name='Price',
            increasing=dict(line=dict(color='green')),
            decreasing=dict(line=dict(color='red')),
            whiskerwidth=0.5,  # Mum çubuklarının genişliğini ayarlıyoruz
            opacity=0.7       # Mumların şeffaflık seviyesini ayarlıyoruz
        )

        # Basit Hareketli Ortalama (SMA) çizgisi oluşturuyoruz
        sma_line = go.Scatter(
            x=self.df.index,
            y=self.df['SMA'],
            line={'color': 'blue', 'width': 2},
            name='SMA'
        )

        # Üssel Hareketli Ortalama (EMA) çizgisi oluşturuyoruz
        ema_line = go.Scatter(
            x=self.df.index,
            y=self.df['EMA'],
            line={'color': 'cyan', 'width': 2},
            name='EMA'
        )

        # Bollinger Bandı üst çizgisi oluşturuyoruz
        upper_bb = go.Scatter(
            x=self.df.index,
            y=self.df['Upper_BB'],
            line={'color': 'red', 'width': 1},
            name='Upper BB'
        )

        # Bollinger Bandı alt çizgisi oluşturuyoruz
        lower_bb = go.Scatter(
            x=self.df.index,
            y=self.df['Lower_BB'],
            line={'color': 'red', 'width': 1},
            name='Lower BB'
        )

        # Bollinger Bandı orta çizgisi oluşturuyoruz
        middle_bb = go.Scatter(
            x=self.df.index,
            y=self.df['Middle_BB'],
            line={'color': 'green', 'width': 1},
            name='Middle BB'
        )

        # Tüm çizgileri grafiğe ekliyoruz
        fig.add_trace(candlestick, row=1, col=1)
        fig.add_trace(sma_line, row=1, col=1)
        fig.add_trace(ema_line, row=1, col=1)
        fig.add_trace(upper_bb, row=1, col=1)
        fig.add_trace(lower_bb, row=1, col=1)
        fig.add_trace(middle_bb, row=1, col=1)

        # RSI çizgisi oluşturuyoruz
        rsi = go.Scatter(
            x=self.df.index,
            y=self.df['RSI'],
            line={'color': 'purple', 'width': 2},
            name='RSI'
        )

        # RSI grafiğine çizgiyi ekliyoruz
        fig.add_trace(rsi, row=2, col=1)

        # Grafik düzenlemelerini yapıyoruz
        fig.update_layout(
            title=f'{self.ticker} Technical Analysis',
            yaxis_title='Price',
            xaxis_title='Date',
            xaxis_rangeslider_visible=False,  # Tarih kaydırıcısını gizle
            height=900,  # Grafik yüksekliği
            template='plotly_dark',  # Grafik teması
            shapes=[
                dict(
                    type='line',
                    x0=self.df.index[0],
                    y0=30,
                    x1=self.df.index[-1],
                    y1=30,
                    line={'color': 'gray', 'width': 1, 'dash': 'dash'}
                ),
                dict(
                    type='line',
                    x0=self.df.index[0],
                    y0=70,
                    x1=self.df.index[-1],
                    y1=70,
                    line={'color': 'gray', 'width': 1, 'dash': 'dash'}
                )
            ]
        )

        # RSI grafiğinin y eksenini 0 ile 100 arasında ayarlıyoruz
        fig.update_yaxes(range=[0, 100], row=2, col=1)

        # Grafik için x ve y eksenlerinin görünümünü ve genişliğini ayarlıyoruz
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray', row=1, col=1)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray', row=1, col=1)
        
        # Grafiği gösteriyoruz
        fig.show()


if __name__ == "__main__":

    # Kullanıcıdan hisse senedi sembolünü ve başlangıç tarihini alıyoruz
    ticker = input("Lütfen hisse sembolünü giriniz: ")
    start_date = input("Lütfen başlangıç tarihini giriniz (YIL-AY-GÜN)")


    # Sınıfı oluşturuyorsunuz ve metodları çağırıyorsunuz
    dashboard = TechnicalAnalysisDashboard(ticker, start_date)
    dashboard.calculate_indicators()
    dashboard.create_plot()
