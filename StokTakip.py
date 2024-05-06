import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Urun:
    def __init__(self, urun_id, ad, stok_miktari):
        self.urun_id = urun_id
        self.ad = ad
        self.stok_miktari = stok_miktari

    def urun_ekle(self, adet):
        self.stok_miktari += adet
        print(f"{adet} adet {self.ad} ürünü stoka eklendi.")

    def siparis_olustur(self, adet):
        if adet <= self.stok_miktari:
            self.stok_miktari -= adet
            print(f"{adet} adet {self.ad} ürünü sipariş edildi.")
        else:
            print("Üzgünüz, yeterli stok bulunmamaktadır.")

    def stok_guncelle(self, adet):
        self.stok_miktari += adet
        print(f"{adet} adet {self.ad} ürününün stok miktarı güncellendi.")

class Stok:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.urun_id] = urun
        print(f"{urun.ad} ürünü stoka eklendi.")

    def stok_durumu_goruntule(self):
        print("Stok Durumu:")
        for urun_id, urun in self.urunler.items():
            print(f"{urun.ad}: {urun.stok_miktari}")

    def urun_ara(self, urun_id):
        if urun_id in self.urunler:
            urun = self.urunler[urun_id]
            print(f"{urun.ad} ürünü bulundu. Stok miktarı: {urun.stok_miktari}")
        else:
            print("Ürün bulunamadı.")

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stok Takip Sistemi")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_urun_ad = QLabel("Ürün Adı:")
        self.input_urun_ad = QLineEdit()
        self.layout.addWidget(self.label_urun_ad)
        self.layout.addWidget(self.input_urun_ad)

        self.label_stok_miktari = QLabel("Stok Miktarı:")
        self.input_stok_miktari = QLineEdit()
        self.layout.addWidget(self.label_stok_miktari)
        self.layout.addWidget(self.input_stok_miktari)

        self.btn_urun_ekle = QPushButton("Ürün Ekle")
        self.btn_urun_ekle.clicked.connect(self.urun_ekle)
        self.layout.addWidget(self.btn_urun_ekle)

        self.btn_stok_durumu_goruntule = QPushButton("Stok Durumu Görüntüle")
        self.btn_stok_durumu_goruntule.clicked.connect(self.stok_durumu_goruntule)
        self.layout.addWidget(self.btn_stok_durumu_goruntule)

        self.liste_urunler = QListWidget()
        self.layout.addWidget(self.liste_urunler)

        self.setLayout(self.layout)

    def urun_ekle(self):
        urun_ad = self.input_urun_ad.text()
        stok_miktari = int(self.input_stok_miktari.text())

        # Ürün oluşturuluyor
        urun = Urun(len(stok.urunler) + 1, urun_ad, stok_miktari)

        # Ürün stoka ekleniyor
        stok.urun_ekle(urun)

        # Ürün listesine ekleniyor
        self.liste_urunler.addItem(f"{urun.ad}: {urun.stok_miktari}")

    def stok_durumu_goruntule(self):
        # Stok durumu görüntüleniyor
        stok.stok_durumu_goruntule()

# Örnek stok oluşturuluyor
stok = Stok()

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

