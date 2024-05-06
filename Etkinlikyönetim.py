import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Etkinlik:
    def __init__(self, etkinlik_id, ad, tarih, yer):
        self.etkinlik_id = etkinlik_id
        self.ad = ad
        self.tarih = tarih
        self.yer = yer

class Katilimci:
    def __init__(self, katilimci_id, ad, soyad, email):
        self.katilimci_id = katilimci_id
        self.ad = ad
        self.soyad = soyad
        self.email = email

class Bilet:
    def __init__(self, bilet_id, etkinlik, katilimci, fiyat):
        self.bilet_id = bilet_id
        self.etkinlik = etkinlik
        self.katilimci = katilimci
        self.fiyat = fiyat

    def bilet_sat(self):
        # Bilet satış işlemi gerçekleştirilir
        print(f"{self.katilimci.ad} {self.katilimci.soyad} için {self.etkinlik.ad} etkinliği için bilet satıldı.")

    def bilet_iptal(self):
        # Bilet iptal işlemi gerçekleştirilir
        print(f"{self.katilimci.ad} {self.katilimci.soyad} için {self.etkinlik.ad} etkinliği için bilet iptal edildi.")

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etkinlik Yönetim Sistemi")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_isim = QLabel("İsim:")
        self.input_isim = QLineEdit()
        self.layout.addWidget(self.label_isim)
        self.layout.addWidget(self.input_isim)

        self.label_soyad = QLabel("Soyad:")
        self.input_soyad = QLineEdit()
        self.layout.addWidget(self.label_soyad)
        self.layout.addWidget(self.input_soyad)

        self.btn_bilet_sat = QPushButton("Bilet Sat")
        self.btn_bilet_sat.clicked.connect(self.bilet_sat)
        self.layout.addWidget(self.btn_bilet_sat)

        self.btn_bilet_iptal = QPushButton("Bilet İptal")
        self.btn_bilet_iptal.clicked.connect(self.bilet_iptal)
        self.layout.addWidget(self.btn_bilet_iptal)

        self.liste_biletler = QListWidget()
        self.layout.addWidget(self.liste_biletler)

        self.setLayout(self.layout)

    def bilet_sat(self):
        isim = self.input_isim.text()
        soyad = self.input_soyad.text()

        # Ödünç alınan biletin bilgileri - Burada eksik olduğu için sabit bilgiler kullanıldı
        etkinlik = Etkinlik(1, "Python Workshop", "25/05/2024", "Online")
        katilimci = Katilimci(101, isim, soyad, "ahmet@example.com")

        # Burada bilet satışı işlemi gerçekleştirilebilir
        bilet = Bilet(1, etkinlik, katilimci, 50)
        bilet.bilet_sat()
        self.liste_biletler.addItem(f"{isim} {soyad} - Bilet Satıldı")

    def bilet_iptal(self):
        secili_item = self.liste_biletler.currentItem()
        if secili_item is not None:
            self.liste_biletler.takeItem(self.liste_biletler.row(secili_item))
            QMessageBox.information(self, "Bilgi", "Bilet başarıyla iptal edildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen iptal edilecek bileti seçin.")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
