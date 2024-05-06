import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

class Kullanici:
    def __init__(self, ad, yas, cinsiyet):
        self.ad = ad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.kayitlar = []

    def kayit_ekle(self, kayit):
        self.kayitlar.append(kayit)

    def egzersiz_ekle(self, egzersiz):
        self.kayitlar.append(egzersiz)

    def rapor_olustur(self):
        # Kullanıcıya ait kayıtlara dayanarak bir rapor oluştur
        pass

class SaglikKaydi:
    def __init__(self, tarih, kan_basinci, kan_sekeri):
        self.tarih = tarih
        self.kan_basinci = kan_basinci
        self.kan_sekeri = kan_sekeri

class Egzersiz:
    def __init__(self, ad, sure, tekrar):
        self.ad = ad
        self.sure = sure
        self.tekrar = tekrar

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_ad = QLabel("Ad:")
        self.input_ad = QLineEdit()
        self.layout.addWidget(self.label_ad)
        self.layout.addWidget(self.input_ad)

        self.label_yas = QLabel("Yaş:")
        self.input_yas = QLineEdit()
        self.layout.addWidget(self.label_yas)
        self.layout.addWidget(self.input_yas)

        self.label_cinsiyet = QLabel("Cinsiyet:")
        self.input_cinsiyet = QLineEdit()
        self.layout.addWidget(self.label_cinsiyet)
        self.layout.addWidget(self.input_cinsiyet)

        self.btn_kayit_ekle = QPushButton("Kayıt Ekle")
        self.btn_kayit_ekle.clicked.connect(self.kayit_ekle)
        self.layout.addWidget(self.btn_kayit_ekle)

        self.btn_egzersiz_ekle = QPushButton("Egzersiz Ekle")
        self.btn_egzersiz_ekle.clicked.connect(self.egzersiz_ekle)
        self.layout.addWidget(self.btn_egzersiz_ekle)

        self.setLayout(self.layout)

    def kayit_ekle(self):
        ad = self.input_ad.text()
        yas = self.input_yas.text()
        cinsiyet = self.input_cinsiyet.text()

        # Kullanıcı oluştur
        kullanici = Kullanici(ad, yas, cinsiyet)

        # Sağlık kaydı oluştur
        saglik_kaydi = SaglikKaydi("2024-05-15", "120/80", "90")

        # Kullanıcıya sağlık kaydı ekle
        kullanici.kayit_ekle(saglik_kaydi)

        QMessageBox.information(self, "Bilgi", "Sağlık kaydı eklendi.")

    def egzersiz_ekle(self):
        ad = self.input_ad.text()
        yas = self.input_yas.text()
        cinsiyet = self.input_cinsiyet.text()

        # Kullanıcı oluştur
        kullanici = Kullanici(ad, yas, cinsiyet)

        # Egzersiz bilgisi oluştur
        egzersiz = Egzersiz("Koşu", "30 dakika", "5 km")

        # Kullanıcıya egzersiz ekleme
        kullanici.egzersiz_ekle(egzersiz)

        QMessageBox.information(self, "Bilgi", "Egzersiz eklendi.")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
