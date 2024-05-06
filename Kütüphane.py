import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Mevcut"  # Varsayılan olarak kitap mevcut

    def durum_guncelle(self, durum):
        self.durum = durum

class Uye:
    def __init__(self, uye_id, ad, soyad):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad

class Odunc:
    def __init__(self):
        self.odunc_listesi = []

    def odunc_al(self, kitap, uye, odunc_tarihi, iade_tarihi):
        if kitap.durum == "Mevcut":
            kitap.durum_guncelle("Ödünç")
            self.odunc_listesi.append((kitap, uye, odunc_tarihi, iade_tarihi))
            print("Kitap ödünç alındı.")
        else:
            print("Kitap mevcut değil.")

    def iade_et(self, kitap):
        for odunc in self.odunc_listesi:
            if odunc[0] == kitap:
                self.odunc_listesi.remove(odunc)
                kitap.durum_guncelle("Mevcut")
                print("Kitap başarıyla iade edildi.")
                return
        print("Bu kitap ödünç alınmamış.")

    def odunc_bilgisi(self):
        for odunc in self.odunc_listesi:
            print(f"Kitap: {odunc[0].ad}, Üye: {odunc[1].ad} {odunc[1].soyad}, Ödünç Tarihi: {odunc[2]}, İade Tarihi: {odunc[3]}")

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kütüphane Yönetim Sistemi")
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

        self.btn_odunc_al = QPushButton("Ödünç Al")
        self.btn_odunc_al.clicked.connect(self.odunc_al)
        self.layout.addWidget(self.btn_odunc_al)

        self.btn_iade_et = QPushButton("İade Et")
        self.btn_iade_et.clicked.connect(self.iade_et)
        self.layout.addWidget(self.btn_iade_et)

        self.liste_odunc = QListWidget()
        self.layout.addWidget(self.liste_odunc)

        self.setLayout(self.layout)

    def odunc_al(self):
        isim = self.input_isim.text()
        soyad = self.input_soyad.text()

        # Ödünç alınan kitabın bilgileri - Burada eksik olduğu için sabit bilgiler kullanıldı
        kitap = Kitap(1, "Python Programming", "John Smith")
        uye = Uye(101, isim, soyad)

        # Burada ödünç alma işlemi gerçekleştirilebilir
        odunc = Odunc()
        odunc_bilgisi = odunc.odunc_al(kitap, uye, "01/05/2024", "15/05/2024")
        self.liste_odunc.addItem(f"{isim} {soyad} - Ödünç Alındı")

    def iade_et(self):
        secili_item = self.liste_odunc.currentItem()
        if secili_item is not None:
            self.liste_odunc.takeItem(self.liste_odunc.row(secili_item))
            QMessageBox.information(self, "Bilgi", "Kitap başarıyla iade edildi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen iade edilecek kitabı seçin.")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

