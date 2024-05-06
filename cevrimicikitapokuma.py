import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget

class Kitap:
    def __init__(self, kitap_adi, yazar, yayinevi):
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yorumlar = []

    def kitap_ekle(self):
        # Kitap ekleme işlemleri
        pass

    def kitap_oku(self):
        # Kitabı okuma işlemleri
        pass

    def yorum_yap(self, yorum):
        self.yorumlar.append(yorum)

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.okuma_listesi = []

    def kitap_ekle_okuma_listesi(self, kitap):
        self.okuma_listesi.append(kitap)

class Yorum:
    def __init__(self, yorum_metni, yorum_yapan_kullanici):
        self.yorum_metni = yorum_metni
        self.yorum_yapan_kullanici = yorum_yapan_kullanici

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Çevrimiçi Kitap Okuma ve Paylaşım Platformu")

        self.kitap_adi_label = QLabel("Kitap Adı:")
        self.kitap_adi_input = QLineEdit()
        self.yazar_label = QLabel("Yazar:")
        self.yazar_input = QLineEdit()
        self.yayinevi_label = QLabel("Yayınevi:")
        self.yayinevi_input = QLineEdit()
        self.kitap_ekle_button = QPushButton("Kitap Ekle")
        self.kitap_ekle_button.clicked.connect(self.kitap_ekle)

        self.yorum_label = QLabel("Yorum:")
        self.yorum_input = QTextEdit()
        self.yorum_yap_button = QPushButton("Yorum Yap")
        self.yorum_yap_button.clicked.connect(self.yorum_yap)

        self.kitaplar_listesi_label = QLabel("Kitaplar:")
        self.kitaplar_listesi = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.kitap_adi_label)
        layout.addWidget(self.kitap_adi_input)
        layout.addWidget(self.yazar_label)
        layout.addWidget(self.yazar_input)
        layout.addWidget(self.yayinevi_label)
        layout.addWidget(self.yayinevi_input)
        layout.addWidget(self.kitap_ekle_button)
        layout.addWidget(self.yorum_label)
        layout.addWidget(self.yorum_input)
        layout.addWidget(self.yorum_yap_button)
        layout.addWidget(self.kitaplar_listesi_label)
        layout.addWidget(self.kitaplar_listesi)

        self.setLayout(layout)

    def kitap_ekle(self):
        kitap_adi = self.kitap_adi_input.text()
        yazar = self.yazar_input.text()
        yayinevi = self.yayinevi_input.text()

        # Yeni bir kitap oluştur
        yeni_kitap = Kitap(kitap_adi, yazar, yayinevi)

        # Kitap listesine eklemek için buraya uygun kodu ekleyin

        # Eklenen kitabı listeye ekle
        self.kitaplar_listesi.addItem(kitap_adi)

    def yorum_yap(self):
        yorum_metni = self.yorum_input.toPlainText()
        secili_kitap = self.kitaplar_listesi.currentItem()

        if secili_kitap:
            # Seçilen kitaba yorum yap
            yorum_yapan_kullanici = "Kullanıcı"  # Burada mevcut kullanıcı bilgisi olmalı
            yorum = Yorum(yorum_metni, yorum_yapan_kullanici)
            secili_kitap.yorum_yap(yorum)
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
