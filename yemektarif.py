import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Tarif:
    def __init__(self, tarif_id, ad, malzemeler, tarif_icerigi):
        self.tarif_id = tarif_id
        self.ad = ad
        self.malzemeler = malzemeler
        self.tarif_icerigi = tarif_icerigi
        self.degerlendirme = None

    def tarif_ekle(self):
        # Yeni bir tarif eklenir
        print(f"{self.ad} tarifi eklendi.")

    def tarif_ara(self, anahtar_kelime):
        # Anahtar kelimeye göre tarif aranır
        print(f"{anahtar_kelime} anahtar kelimesine göre tarif aranıyor...")

    def tarif_degerlendir(self, puan):
        # Tarife puan verilir
        self.degerlendirme = puan
        print(f"{self.ad} tarifi {puan} puanla değerlendirildi.")

class Malzeme:
    def __init__(self, malzeme_id, ad, miktar):
        self.malzeme_id = malzeme_id
        self.ad = ad
        self.miktar = miktar

class Kullanici:
    def __init__(self, kullanici_id, kullanici_ad, sifre):
        self.kullanici_id = kullanici_id
        self.kullanici_ad = kullanici_ad
        self.sifre = sifre

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yemek Tarifi Uygulaması")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_tarif_adi = QLabel("Tarif Adı:")
        self.input_tarif_adi = QLineEdit()
        self.layout.addWidget(self.label_tarif_adi)
        self.layout.addWidget(self.input_tarif_adi)

        self.label_malzemeler = QLabel("Malzemeler:")
        self.input_malzemeler = QLineEdit()
        self.layout.addWidget(self.label_malzemeler)
        self.layout.addWidget(self.input_malzemeler)

        self.label_tarif_icerigi = QLabel("Tarif İçeriği:")
        self.input_tarif_icerigi = QLineEdit()
        self.layout.addWidget(self.label_tarif_icerigi)
        self.layout.addWidget(self.input_tarif_icerigi)

        self.btn_tarif_ekle = QPushButton("Tarif Ekle")
        self.btn_tarif_ekle.clicked.connect(self.tarif_ekle)
        self.layout.addWidget(self.btn_tarif_ekle)

        self.btn_tarif_ara = QPushButton("Tarif Ara")
        self.btn_tarif_ara.clicked.connect(self.tarif_ara)
        self.layout.addWidget(self.btn_tarif_ara)

        self.liste_tarifler = QListWidget()
        self.layout.addWidget(self.liste_tarifler)

        self.setLayout(self.layout)

    def tarif_ekle(self):
        tarif_adi = self.input_tarif_adi.text()
        malzemeler = self.input_malzemeler.text()
        tarif_icerigi = self.input_tarif_icerigi.text()

        # Yeni bir tarif oluşturuluyor
        tarif = Tarif(1, tarif_adi, malzemeler, tarif_icerigi)
        tarif.tarif_ekle()
        self.liste_tarifler.addItem(tarif_adi)

    def tarif_ara(self):
        anahtar_kelime = self.input_tarif_adi.text()

        # Anahtar kelimeye göre tarif aranıyor
        tarif = Tarif(1, "", "", "")
        tarif.tarif_ara(anahtar_kelime)

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
