import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QListWidget

class Ders:
    def __init__(self, ders_adi, icerik, ogretmen):
        self.ders_adi = ders_adi
        self.icerik = icerik
        self.ogretmen = ogretmen
        self.materyaller = []

    def materyal_yukle(self, materyal):
        self.materyaller.append(materyal)

    def materyal_eris(self):
        # Materyallere erişim işlemleri
        pass

    def soru_sor(self):
        # Dersle ilgili soru sorma işlemleri
        pass

class Ogrenci:
    def __init__(self, ogrenci_adi, numara):
        self.ogrenci_adi = ogrenci_adi
        self.numara = numara
        self.katilim_durumu = False

    def katil(self):
        self.katilim_durumu = True

class Materyal:
    def __init__(self, materyal_adi, turu, icerik):
        self.materyal_adi = materyal_adi
        self.turu = turu
        self.icerik = icerik

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Eğitim Materyali Paylaşım Platformu")

        self.ders_adi_label = QLabel("Ders Adı:")
        self.ders_adi_input = QLineEdit()
        self.icerik_label = QLabel("İçerik:")
        self.icerik_input = QLineEdit()
        self.ogretmen_label = QLabel("Öğretmen:")
        self.ogretmen_input = QLineEdit()

        self.ders_ekle_button = QPushButton("Ders Ekle")
        self.ders_ekle_button.clicked.connect(self.ders_ekle)

        self.ders_listesi_label = QLabel("Ders Listesi:")
        self.ders_listesi = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.ders_adi_label)
        layout.addWidget(self.ders_adi_input)
        layout.addWidget(self.icerik_label)
        layout.addWidget(self.icerik_input)
        layout.addWidget(self.ogretmen_label)
        layout.addWidget(self.ogretmen_input)
        layout.addWidget(self.ders_ekle_button)
        layout.addWidget(self.ders_listesi_label)
        layout.addWidget(self.ders_listesi)

        self.setLayout(layout)

    def ders_ekle(self):
        ders_adi = self.ders_adi_input.text()
        icerik = self.icerik_input.text()
        ogretmen = self.ogretmen_input.text()

        # Yeni bir ders oluştur
        yeni_ders = Ders(ders_adi, icerik, ogretmen)

        # Ders listesine ekle
        self.ders_listesi.addItem(ders_adi)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
