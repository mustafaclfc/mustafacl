import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from functools import partial

class AracKiralamaArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Araç Kiralama Sistemi")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.arac_listesi = QListWidget()
        layout.addWidget(QLabel("Araç Listesi:"))
        layout.addWidget(self.arac_listesi)

        self.musteri_id_label = QLabel("Müşteri ID:")
        self.musteri_id_input = QLineEdit()
        layout.addWidget(self.musteri_id_label)
        layout.addWidget(self.musteri_id_input)

        self.kiralama_button = QPushButton("Araç Kirala")
        layout.addWidget(self.kiralama_button)

        self.setLayout(layout)

        self.arac_listesi.addItems(["Renault Clio", "Volkswagen Golf", "Ford Focus"])

        self.kiralama_button.clicked.connect(self.arac_kirala)

    def arac_kirala(self):
        arac_adi = self.arac_listesi.currentItem().text()
        musteri_id = self.musteri_id_input.text()

        if not musteri_id:
            QMessageBox.warning(self, "Uyarı", "Müşteri ID'si girilmedi!")
            return

        QMessageBox.information(self, "Bilgi", f"{arac_adi} aracı {musteri_id} ID'li müşteriye kiralama işlemi gerçekleştirildi.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AracKiralamaArayuzu()
    window.show()
    sys.exit(app.exec_())
