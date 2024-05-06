import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QComboBox, QCalendarWidget

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hastane Randevu Sistemi")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_isim = QLabel("İsim:")
        self.input_isim = QLineEdit()
        self.layout.addWidget(self.label_isim)
        self.layout.addWidget(self.input_isim)

        self.label_tc = QLabel("TC:")
        self.input_tc = QLineEdit()
        self.layout.addWidget(self.label_tc)
        self.layout.addWidget(self.input_tc)

        self.label_doktor = QLabel("Doktor:")
        self.combo_doktor = QComboBox()
        self.combo_doktor.addItems(["Dr. Ahmet", "Dr. Mehmet", "Dr. Ayşe"])
        self.layout.addWidget(self.label_doktor)
        self.layout.addWidget(self.combo_doktor)

        self.label_tarih = QLabel("Tarih:")
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.label_tarih)
        self.layout.addWidget(self.calendar)

        self.btn_randevu_al = QPushButton("Randevu Al")
        self.btn_randevu_al.clicked.connect(self.randevu_al)
        self.layout.addWidget(self.btn_randevu_al)

        self.setLayout(self.layout)

    def randevu_al(self):
        isim = self.input_isim.text()
        tc = self.input_tc.text()
        doktor = self.combo_doktor.currentText()
        tarih = self.calendar.selectedDate().toString("dd-MM-yyyy")

        # Burada randevu alınma işlemi gerçekleştirilebilir
        QMessageBox.information(self, "Bilgi", f"{isim}, {doktor} için {tarih} tarihinde randevu alındı.")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
class Hasta:
    def __init__(self, isim, tc):
        self.isim = isim
        self.tc = tc
        self.randevu_gecmisi = []

class Doktor:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.musaitlik_durumu = True  # Varsayılan olarak müsait

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

class RandevuSistemi:
    def __init__(self):
        self.doktorlar = []
        self.hastalar = []
        self.randevular = []

    def doktor_ekle(self, doktor):
        self.doktorlar.append(doktor)

    def hasta_ekle(self, hasta):
        self.hastalar.append(hasta)

    def randevu_al(self, hasta, doktor, tarih):
        if doktor.musaitlik_durumu:
            randevu = Randevu(tarih, doktor, hasta)
            self.randevular.append(randevu)
            doktor.musaitlik_durumu = False
            hasta.randevu_gecmisi.append(randevu)
            print("Randevu başarıyla oluşturuldu.")
        else:
            print("Doktor müsait değil.")

    def randevu_iptal(self, hasta, randevu):
        if randevu in hasta.randevu_gecmisi:
            self.randevular.remove(randevu)
            doktor = randevu.doktor
            doktor.musaitlik_durumu = True
            hasta.randevu_gecmisi.remove(randevu)
            print("Randevu başarıyla iptal edildi.")
        else:
            print("Geçersiz randevu.")
