import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Etkinlik:
    def __init__(self, ad, tarih, mekan):
        self.ad = ad
        self.tarih = tarih
        self.mekan = mekan

    def etkinlik_ekle(self):
        # Etkinlik ekleme işlemleri
        pass

    def bilet_sat(self):
        # Bilet satışı yapma işlemleri
        pass

class Bilet:
    def __init__(self, numara, etkinlik):
        self.numara = numara
        self.etkinlik = etkinlik

class Kullanici:
    def __init__(self, ad, soyad, email):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.biletler = []

    def bilet_al(self, bilet):
        self.biletler.append(bilet)

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etkinlik ve Bilet Satış Platformu")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_ad = QLabel("Etkinlik Adı:")
        self.input_ad = QLineEdit()
        self.layout.addWidget(self.label_ad)
        self.layout.addWidget(self.input_ad)

        self.label_tarih = QLabel("Tarih:")
        self.input_tarih = QLineEdit()
        self.layout.addWidget(self.label_tarih)
        self.layout.addWidget(self.input_tarih)

        self.label_mekan = QLabel("Mekan:")
        self.input_mekan = QLineEdit()
        self.layout.addWidget(self.label_mekan)
        self.layout.addWidget(self.input_mekan)

        self.btn_etkinlik_ekle = QPushButton("Etkinlik Ekle")
        self.btn_etkinlik_ekle.clicked.connect(self.etkinlik_ekle)
        self.layout.addWidget(self.btn_etkinlik_ekle)

        self.liste_biletler = QListWidget()
        self.layout.addWidget(self.liste_biletler)

        self.setLayout(self.layout)

    def etkinlik_ekle(self):
        ad = self.input_ad.text()
        tarih = self.input_tarih.text()
        mekan = self.input_mekan.text()

        # Burada etkinlik ekleme işlemi gerçekleştirilebilir
        # Ardından eklenen etkinlik bilgileri listeye eklenebilir
        self.liste_biletler.addItem(f"{ad} - {tarih} - {mekan}")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
