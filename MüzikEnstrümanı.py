import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget

class Enstruman:
    def __init__(self, ad, stok_miktari):
        self.ad = ad
        self.stok_miktari = stok_miktari

class Satis:
    def __init__(self, siparis_no, satilan_enstrumanlar):
        self.siparis_no = siparis_no
        self.satilan_enstrumanlar = satilan_enstrumanlar

class Destek:
    def __init__(self, talep_no, talep_detaylari):
        self.talep_no = talep_no
        self.talep_detaylari = talep_detaylari

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Müzik Enstrümanı Dükkanı Yönetimi")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Enstrüman ekleme bölümü
        self.label_enstruman_adi = QLabel("Enstrüman Adı:")
        self.input_enstruman_adi = QLineEdit()
        self.layout.addWidget(self.label_enstruman_adi)
        self.layout.addWidget(self.input_enstruman_adi)

        self.label_stok_miktari = QLabel("Stok Miktarı:")
        self.input_stok_miktari = QLineEdit()
        self.layout.addWidget(self.label_stok_miktari)
        self.layout.addWidget(self.input_stok_miktari)

        self.btn_enstruman_ekle = QPushButton("Enstrüman Ekle")
        self.btn_enstruman_ekle.clicked.connect(self.enstruman_ekle)
        self.layout.addWidget(self.btn_enstruman_ekle)

        # Sipariş bölümü
        self.label_siparis_no = QLabel("Sipariş No:")
        self.input_siparis_no = QLineEdit()
        self.layout.addWidget(self.label_siparis_no)
        self.layout.addWidget(self.input_siparis_no)

        self.label_satilan_enstrumanlar = QLabel("Satılan Enstrümanlar:")
        self.input_satilan_enstrumanlar = QLineEdit()
        self.layout.addWidget(self.label_satilan_enstrumanlar)
        self.layout.addWidget(self.input_satilan_enstrumanlar)

        self.btn_satis_yap = QPushButton("Satış Yap")
        self.btn_satis_yap.clicked.connect(self.satis_yap)
        self.layout.addWidget(self.btn_satis_yap)

        # Destek talebi bölümü
        self.label_talep_no = QLabel("Talep No:")
        self.input_talep_no = QLineEdit()
        self.layout.addWidget(self.label_talep_no)
        self.layout.addWidget(self.input_talep_no)

        self.label_talep_detaylari = QLabel("Talep Detayları:")
        self.input_talep_detaylari = QLineEdit()
        self.layout.addWidget(self.label_talep_detaylari)
        self.layout.addWidget(self.input_talep_detaylari)

        self.btn_destek_olustur = QPushButton("Destek Talebi Oluştur")
        self.btn_destek_olustur.clicked.connect(self.destek_olustur)
        self.layout.addWidget(self.btn_destek_olustur)

        # Enstrümanları görüntüleme bölümü
        self.label_enstrumanlar = QLabel("Enstrümanlar:")
        self.liste_enstrumanlar = QListWidget()
        self.layout.addWidget(self.label_enstrumanlar)
        self.layout.addWidget(self.liste_enstrumanlar)

        self.setLayout(self.layout)

    def enstruman_ekle(self):
        enstruman_adi = self.input_enstruman_adi.text()
        stok_miktari = self.input_stok_miktari.text()
        enstruman = Enstruman(enstruman_adi, stok_miktari)
        self.liste_enstrumanlar.addItem(f"{enstruman_adi} - Stok: {stok_miktari}")

    def satis_yap(self):
        siparis_no = self.input_siparis_no.text()
        satilan_enstrumanlar = self.input_satilan_enstrumanlar.text()
        satis = Satis(siparis_no, satilan_enstrumanlar)
        self.liste_enstrumanlar.addItem(f"Sipariş No: {siparis_no}, Satılan Enstrümanlar: {satilan_enstrumanlar}")

    def destek_olustur(self):
        talep_no = self.input_talep_no.text()
        talep_detaylari = self.input_talep_detaylari.text()
        destek = Destek(talep_no, talep_detaylari)
        self.liste_enstrumanlar.addItem(f"Destek Talep No: {talep_no}, Detaylar: {talep_detaylari}")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
