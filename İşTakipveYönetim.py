import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

from datetime import datetime

class Proje:
    def __init__(self, proje_adi, baslangic_tarihi, bitis_tarihi):
        self.proje_adi = proje_adi
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi
        self.gorevler = []

    def proje_olustur(self):
        # Proje oluşturma işlemleri
        pass

    def gorev_ata(self, gorev):
        self.gorevler.append(gorev)

    def ilerleme_kaydet(self, gorev_adi, ilerleme):
        for gorev in self.gorevler:
            if gorev.gorev_adi == gorev_adi:
                gorev.ilerleme = ilerleme

class Gorev:
    def __init__(self, gorev_adi, sorumlu_kisi):
        self.gorev_adi = gorev_adi
        self.sorumlu_kisi = sorumlu_kisi
        self.ilerleme = 0

class Calisan:
    def __init__(self, calisan_adi):
        self.calisan_adi = calisan_adi
        self.gorevleri = []

    def gorev_ekle(self, gorev):
        self.gorevleri.append(gorev)

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("İş Takip ve Yönetim Sistemi")

        self.proje_adi_label = QLabel("Proje Adı:")
        self.proje_adi_input = QLineEdit()
        self.baslangic_tarihi_label = QLabel("Başlangıç Tarihi:")
        self.baslangic_tarihi_input = QLineEdit()
        self.bitis_tarihi_label = QLabel("Bitiş Tarihi:")
        self.bitis_tarihi_input = QLineEdit()

        self.proje_olustur_button = QPushButton("Proje Oluştur")
        self.proje_olustur_button.clicked.connect(self.proje_olustur)

        self.gorevler_listesi_label = QLabel("Görevler:")
        self.gorevler_listesi = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.proje_adi_label)
        layout.addWidget(self.proje_adi_input)
        layout.addWidget(self.baslangic_tarihi_label)
        layout.addWidget(self.baslangic_tarihi_input)
        layout.addWidget(self.bitis_tarihi_label)
        layout.addWidget(self.bitis_tarihi_input)
        layout.addWidget(self.proje_olustur_button)
        layout.addWidget(self.gorevler_listesi_label)
        layout.addWidget(self.gorevler_listesi)

        self.setLayout(layout)

    def proje_olustur(self):
        proje_adi = self.proje_adi_input.text()
        baslangic_tarihi = self.baslangic_tarihi_input.text()
        bitis_tarihi = self.bitis_tarihi_input.text()

        # Yeni bir proje oluştur
        yeni_proje = Proje(proje_adi, baslangic_tarihi, bitis_tarihi)

        # Proje listesine eklemek için buraya uygun kodu ekleyin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
