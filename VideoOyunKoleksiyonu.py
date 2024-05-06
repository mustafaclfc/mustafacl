import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class Oyun:
    def __init__(self, oyun_adi, turu, platformu):
        self.oyun_adi = oyun_adi
        self.turu = turu
        self.platformu = platformu

    def oyun_ekle(self):
        # Oyun ekleme işlemleri
        pass

    def degerlendir(self, oyuncu, puan):
        # Oyunun değerlendirilmesi işlemleri
        pass

    def oneri_al(self):
        # Oyun önerisi alma işlemleri
        pass

class Koleksiyon:
    def __init__(self):
        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

class Oyuncu:
    def __init__(self, oyuncu_adi):
        self.oyuncu_adi = oyuncu_adi
        self.favori_oyunlar = []
        self.koleksiyon = Koleksiyon()

    def favori_oyun_ekle(self, oyun):
        self.favori_oyunlar.append(oyun)

    def koleksiyona_oyun_ekle(self, oyun):
        self.koleksiyon.oyun_ekle(oyun)

class OyunArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Oyun Koleksiyonu Yönetimi")
        self.init_ui()

    def init_ui(self):
        self.oyun_adi_label = QLabel("Oyun Adı:")
        self.oyun_adi_entry = QLineEdit()
        self.turu_label = QLabel("Türü:")
        self.turu_entry = QLineEdit()
        self.platformu_label = QLabel("Platformu:")
        self.platformu_entry = QLineEdit()

        self.ekle_button = QPushButton("Oyun Ekle")
        self.ekle_button.clicked.connect(self.oyun_ekle)

        v_box = QVBoxLayout()
        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.oyun_adi_label)
        h_box1.addWidget(self.oyun_adi_entry)
        v_box.addLayout(h_box1)
        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.turu_label)
        h_box2.addWidget(self.turu_entry)
        v_box.addLayout(h_box2)
        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.platformu_label)
        h_box3.addWidget(self.platformu_entry)
        v_box.addLayout(h_box3)

        v_box.addWidget(self.ekle_button)

        self.setLayout(v_box)

    def oyun_ekle(self):
        oyun_adi = self.oyun_adi_entry.text()
        turu = self.turu_entry.text()
        platformu = self.platformu_entry.text()

        # Burada oyun eklemesi yapılabilir, mevcut sınıfları kullanarak işlemler gerçekleştirilebilir.

        self.oyun_adi_entry.clear()
        self.turu_entry.clear()
       
