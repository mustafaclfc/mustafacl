import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class Film:
    def __init__(self, film_adi, yonetmen, turu):
        self.film_adi = film_adi
        self.yonetmen = yonetmen
        self.turu = turu

    def film_ekle(self):
        # Film ekleme işlemleri
        pass

    def liste_oluştur(self):
        # İzleme listesi oluşturma işlemleri
        pass

    def içerik_izle(self):
        # İçeriği izleme işlemleri
        pass

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.izleme_gecmisi = []

    def izleme_gecmisi_ekle(self, icerik):
        self.izleme_gecmisi.append(icerik)

class İçerik:
    def __init__(self, icerik_adi, suresi, turu):
        self.icerik_adi = icerik_adi
        self.suresi = suresi
        self.turu = turu

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Film ve Dizi İzleme Servisi")
        self.setGeometry(100, 100, 400, 300)

        self.kullanici_adi_label = QLabel("Kullanıcı Adı:")
        self.kullanici_adi_input = QLineEdit()
        self.sifre_label = QLabel("Şifre:")
        self.sifre_input = QLineEdit()
        self.sifre_input.setEchoMode(QLineEdit.Password)

        self.giris_button = QPushButton("Giriş Yap")
        self.giris_button.clicked.connect(self.giris_yap)

        layout = QVBoxLayout()
        layout.addWidget(self.kullanici_adi_label)
        layout.addWidget(self.kullanici_adi_input)
        layout.addWidget(self.sifre_label)
        layout.addWidget(self.sifre_input)
        layout.addWidget(self.giris_button)

        self.setLayout(layout)

    def giris_yap(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()

        # Kullanıcı adı ve şifrenin doğruluğunu kontrol et
        # Burada kullanıcı adı ve şifre doğruysa ana menü arayüzünü göstermeliyiz
        # Eğer yanlışsa bir hata mesajı göstermeliyiz
        if kullanici_adi == "alice" and sifre == "123456":
            self.show_ana_menu()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")

    def show_ana_menu(self):
        # Ana menü arayüzünü göster
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
