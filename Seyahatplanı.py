import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QListWidgetItem

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seyahat Planlama Uygulaması")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Rota ekleme bölümü
        self.label_rota = QLabel("Seyahat Rotası:")
        self.input_rota = QLineEdit()
        self.layout.addWidget(self.label_rota)
        self.layout.addWidget(self.input_rota)

        self.btn_rota_ekle = QPushButton("Rota Ekle")
        self.btn_rota_ekle.clicked.connect(self.rota_ekle)
        self.layout.addWidget(self.btn_rota_ekle)

        # Konaklama seçimi bölümü
        self.label_konaklama = QLabel("Konaklama Seçeneği:")
        self.input_konaklama = QLineEdit()
        self.layout.addWidget(self.label_konaklama)
        self.layout.addWidget(self.input_konaklama)

        self.btn_konaklama_sec = QPushButton("Konaklama Seç")
        self.btn_konaklama_sec.clicked.connect(self.konaklama_sec)
        self.layout.addWidget(self.btn_konaklama_sec)

        # Seyahat planı gösterme bölümü
        self.label_seyahat_planı = QLabel("Seyahat Planı:")
        self.liste_seyahat_planı = QListWidget()
        self.layout.addWidget(self.label_seyahat_planı)
        self.layout.addWidget(self.liste_seyahat_planı)

        self.setLayout(self.layout)

    def rota_ekle(self):
        rota_detaylari = self.input_rota.text()
        self.liste_seyahat_planı.addItem(f"Seyahat Rotası: {rota_detaylari}")

    def konaklama_sec(self):
        konaklama_secenekleri = self.input_konaklama.text()
        self.liste_seyahat_planı.addItem(f"Konaklama Seçeneği: {konaklama_secenekleri}")

def main():
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
