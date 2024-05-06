import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit

class RestoranUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Restoran Sipariş ve Yönetim Sistemi')
        self.setGeometry(100, 100, 400, 300)

        # Kullanıcı arayüzü bileşenlerinin oluşturulması
        self.label_urun_adi = QLabel('Ürün Adı:')
        self.edit_urun_adi = QLineEdit()
        self.label_fiyat = QLabel('Fiyat:')
        self.edit_fiyat = QLineEdit()
        self.label_stok_durumu = QLabel('Stok Durumu:')
        self.edit_stok_durumu = QLineEdit()

        self.button_urun_ekle = QPushButton('Ürün Ekle')
        self.button_urun_ekle.clicked.connect(self.urun_ekle)

        self.label_siparis_icerik = QLabel('Sipariş İçeriği:')
        self.edit_siparis_icerik = QTextEdit()
        self.label_musteri_adi = QLabel('Müşteri Adı:')
        self.edit_musteri_adi = QLineEdit()
        self.label_adres = QLabel('Adres:')
        self.edit_adres = QLineEdit()

        self.button_siparis_ver = QPushButton('Sipariş Ver')
        self.button_siparis_ver.clicked.connect(self.siparis_ver)

        # Dikey düzen oluşturma ve bileşenleri ekleme
        v_box = QVBoxLayout()
        v_box.addWidget(self.label_urun_adi)
        v_box.addWidget(self.edit_urun_adi)
        v_box.addWidget(self.label_fiyat)
        v_box.addWidget(self.edit_fiyat)
        v_box.addWidget(self.label_stok_durumu)
        v_box.addWidget(self.edit_stok_durumu)
        v_box.addWidget(self.button_urun_ekle)
        v_box.addStretch()
        v_box.addWidget(self.label_siparis_icerik)
        v_box.addWidget(self.edit_siparis_icerik)
        v_box.addWidget(self.label_musteri_adi)
        v_box.addWidget(self.edit_musteri_adi)
        v_box.addWidget(self.label_adres)
        v_box.addWidget(self.edit_adres)
        v_box.addWidget(self.button_siparis_ver)

        self.setLayout(v_box)

    def urun_ekle(self):
        urun_adi = self.edit_urun_adi.text()
        fiyat = self.edit_fiyat.text()
        stok_durumu = self.edit_stok_durumu.text()

        # Ürün ekleme işlemleri burada yapılabilir

        # Test amaçlı, eklenen ürün bilgilerini yazdıralım
        print("Yeni Ürün Eklendi:")
        print("Ürün Adı:", urun_adi)
        print("Fiyat:", fiyat)
        print("Stok Durumu:", stok_durumu)

    def siparis_ver(self):
        siparis_icerik = self.edit_siparis_icerik.toPlainText()
        musteri_adi = self.edit_musteri_adi.text()
        adres = self.edit_adres.text()

        # Sipariş verme işlemleri burada yapılabilir

        # Test amaçlı, verilen sipariş bilgilerini yazdıralım
        print("Yeni Sipariş Verildi:")
        print("Sipariş İçeriği:", siparis_icerik)
        print("Müşteri Adı:", musteri_adi)
        print("Adres:", adres)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    restoran_app = RestoranUygulamasi()
    restoran_app.show()
    sys.exit(app.exec_())

