import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Kurs:
    def __init__(self, kurs_id, ad, egitmen, icerik):
        self.kurs_id = kurs_id
        self.ad = ad
        self.egitmen = egitmen
        self.icerik = icerik
        self.ogrenciler = []

    def kurs_olustur(self):
        # Yeni bir kurs oluşturma işlemi gerçekleştirilir
        print(f"{self.ad} adlı kurs oluşturuldu.")

    def kaydol(self, ogrenci):
        # Öğrencinin kursa kaydolma işlemi gerçekleştirilir
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.ad} kursa kaydoldu.")

    def icerik_yukle(self, icerik):
        # Kurs içeriği yüklenir
        self.icerik = icerik
        print("Kurs içeriği güncellendi.")

class Egitmen:
    def __init__(self, egitmen_id, ad, uzmanlik):
        self.egitmen_id = egitmen_id
        self.ad = ad
        self.uzmanlik = uzmanlik

class Ogrenci:
    def __init__(self, ogrenci_id, ad, email):
        self.ogrenci_id = ogrenci_id
        self.ad = ad
        self.email = email

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Eğitim Platformu")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_isim = QLabel("İsim:")
        self.input_isim = QLineEdit()
        self.layout.addWidget(self.label_isim)
        self.layout.addWidget(self.input_isim)

        self.label_email = QLabel("E-posta:")
        self.input_email = QLineEdit()
        self.layout.addWidget(self.label_email)
        self.layout.addWidget(self.input_email)

        self.btn_kaydol = QPushButton("Kaydol")
        self.btn_kaydol.clicked.connect(self.kaydol)
        self.layout.addWidget(self.btn_kaydol)

        self.btn_icerik_yukle = QPushButton("İçerik Yükle")
        self.btn_icerik_yukle.clicked.connect(self.icerik_yukle)
        self.layout.addWidget(self.btn_icerik_yukle)

        self.liste_kurslar = QListWidget()
        self.layout.addWidget(self.liste_kurslar)

        self.setLayout(self.layout)

    def kaydol(self):
        isim = self.input_isim.text()
        email = self.input_email.text()

        # Öğrenci oluşturuluyor
        ogrenci = Ogrenci(1, isim, email)

        # Kursa kaydolunuyor
        kurs.kaydol(ogrenci)
        self.liste_kurslar.addItem(f"{isim} - Kaydoldu")

    def icerik_yukle(self):
        icerik = "Python temelleri"  # Örnek içerik
        kurs.icerik_yukle(icerik)
        QMessageBox.information(self, "Bilgi", "Kurs içeriği güncellendi.")

# Örnek kullanım
if __name__ == "__main__":
    # Eğitmen oluşturuluyor
    egitmen = Egitmen(1, "Ahmet Yılmaz", "Python")

    # Kurs oluşturuluyor
    kurs = Kurs(1, "Python Programlama", egitmen, "Henüz içerik yok")

    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())
