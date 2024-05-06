import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget

class Sporcu:
    def __init__(self, sporcu_id, ad, spor_dali):
        self.sporcu_id = sporcu_id
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenmanlar = []
        self.takip = {}

    def program_oluştur(self, antrenman):
        self.antrenmanlar.append(antrenman)
        print(f"{self.ad} için {antrenman.ad} adlı antrenman programı oluşturuldu.")

    def ilerleme_kaydet(self, antrenman, ilerleme):
        self.takip[antrenman.ad] = ilerleme
        print(f"{self.ad} için {antrenman.ad} adlı antrenmanın ilerlemesi kaydedildi.")

    def rapor_al(self):
        print(f"{self.ad} için antrenman raporu:")
        for antrenman, ilerleme in self.takip.items():
            print(f"{antrenman}: {ilerleme}")

class Antrenman:
    def __init__(self, antrenman_id, ad, detaylar):
        self.antrenman_id = antrenman_id
        self.ad = ad
        self.detaylar = detaylar

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spor Takip Uygulaması")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_sporcu_ad = QLabel("Sporcu Adı:")
        self.input_sporcu_ad = QLineEdit()
        self.layout.addWidget(self.label_sporcu_ad)
        self.layout.addWidget(self.input_sporcu_ad)

        self.label_spor_dali = QLabel("Spor Dalı:")
        self.input_spor_dali = QLineEdit()
        self.layout.addWidget(self.label_spor_dali)
        self.layout.addWidget(self.input_spor_dali)

        self.label_antrenman_ad = QLabel("Antrenman Adı:")
        self.input_antrenman_ad = QLineEdit()
        self.layout.addWidget(self.label_antrenman_ad)
        self.layout.addWidget(self.input_antrenman_ad)

        self.label_antrenman_detay = QLabel("Antrenman Detayları:")
        self.input_antrenman_detay = QLineEdit()
        self.layout.addWidget(self.label_antrenman_detay)
        self.layout.addWidget(self.input_antrenman_detay)

        self.btn_program_olustur = QPushButton("Program Oluştur")
        self.btn_program_olustur.clicked.connect(self.program_olustur)
        self.layout.addWidget(self.btn_program_olustur)

        self.btn_ilerleme_kaydet = QPushButton("İlerleme Kaydet")
        self.btn_ilerleme_kaydet.clicked.connect(self.ilerleme_kaydet)
        self.layout.addWidget(self.btn_ilerleme_kaydet)

        self.btn_rapor_al = QPushButton("Rapor Al")
        self.btn_rapor_al.clicked.connect(self.rapor_al)
        self.layout.addWidget(self.btn_rapor_al)

        self.setLayout(self.layout)

    def program_olustur(self):
        sporcu_ad = self.input_sporcu_ad.text()
        spor_dali = self.input_spor_dali.text()
        antrenman_ad = self.input_antrenman_ad.text()
        antrenman_detay = self.input_antrenman_detay.text()

        # Sporcu oluşturuluyor
        sporcu = Sporcu(1, sporcu_ad, spor_dali)

        # Antrenman oluşturuluyor
        antrenman = Antrenman(1, antrenman_ad, antrenman_detay)

        # Sporcu için antrenman programı oluşturuluyor
        sporcu.program_oluştur(antrenman)

    def ilerleme_kaydet(self):
        sporcu_ad = self.input_sporcu_ad.text()
        antrenman_ad = self.input_antrenman_ad.text()
        ilerleme = self.input_antrenman_detay.text()

        # Sporcu oluşturuluyor
        sporcu = Sporcu(1, sporcu_ad, "")

        # İlerleme kaydediliyor
        sporcu.ilerleme_kaydet(Antrenman(1, antrenman_ad, ""), ilerleme)

    def rapor_al(self):
        sporcu_ad = self.input_sporcu_ad.text()

        # Sporcu oluşturuluyor
        sporcu = Sporcu(1, sporcu_ad, "")

        # Rapor alınıyor
        sporcu.rapor_al()

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
