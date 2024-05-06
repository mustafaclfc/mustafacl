import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QListWidgetItem

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Müşteri İlişkileri Yönetimi (CRM)")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Müşteri bilgileri bölümü
        self.label_musteri_adi = QLabel("Müşteri Adı:")
        self.input_musteri_adi = QLineEdit()
        self.layout.addWidget(self.label_musteri_adi)
        self.layout.addWidget(self.input_musteri_adi)

        self.label_iletisim_bilgileri = QLabel("İletişim Bilgileri:")
        self.input_iletisim_bilgileri = QLineEdit()
        self.layout.addWidget(self.label_iletisim_bilgileri)
        self.layout.addWidget(self.input_iletisim_bilgileri)

        # Satış ekleme bölümü
        self.label_satis_no = QLabel("Satış No:")
        self.input_satis_no = QLineEdit()
        self.layout.addWidget(self.label_satis_no)
        self.layout.addWidget(self.input_satis_no)

        self.label_satilan_urunler = QLabel("Satılan Ürünler:")
        self.input_satilan_urunler = QLineEdit()
        self.layout.addWidget(self.label_satilan_urunler)
        self.layout.addWidget(self.input_satilan_urunler)

        self.btn_satis_ekle = QPushButton("Satış Ekle")
        self.btn_satis_ekle.clicked.connect(self.satis_ekle)
        self.layout.addWidget(self.btn_satis_ekle)

        # Destek talebi oluşturma bölümü
        self.label_talep_no = QLabel("Talep No:")
        self.input_talep_no = QLineEdit()
        self.layout.addWidget(self.label_talep_no)
        self.layout.addWidget(self.input_talep_no)

        self.label_talep_detaylari = QLabel("Talep Detayları:")
        self.input_talep_detaylari = QLineEdit()
        self.layout.addWidget(self.label_talep_detaylari)
        self.layout.addWidget(self.input_talep_detaylari)

        self.btn_talep_olustur = QPushButton("Talep Oluştur")
        self.btn_talep_olustur.clicked.connect(self.talep_olustur)
        self.layout.addWidget(self.btn_talep_olustur)

        # Müşteri bilgileri görüntüleme bölümü
        self.label_musteri_bilgileri = QLabel("Müşteri Bilgileri:")
        self.liste_musteri_bilgileri = QListWidget()
        self.layout.addWidget(self.label_musteri_bilgileri)
        self.layout.addWidget(self.liste_musteri_bilgileri)

        self.setLayout(self.layout)

    def satis_ekle(self):
        musteri_adi = self.input_musteri_adi.text()
        satis_no = self.input_satis_no.text()
        satilan_urunler = self.input_satilan_urunler.text()
        self.liste_musteri_bilgileri.addItem(f"{musteri_adi} - Satış No: {satis_no}, Ürünler: {satilan_urunler}")

    def talep_olustur(self):
        musteri_adi = self.input_musteri_adi.text()
        talep_no = self.input_talep_no.text()
        talep_detaylari = self.input_talep_detaylari.text()
        self.liste_musteri_bilgileri.addItem(f"{musteri_adi} - Talep No: {talep_no}, Detaylar: {talep_detaylari}")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
