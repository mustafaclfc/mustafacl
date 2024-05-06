class Olay:
    def __init__(self, olay_adi, tarih, aciklama):
        self.olay_adi = olay_adi
        self.tarih = tarih
        self.aciklama = aciklama

    def olay_ekle(self):
        # Olay ekleme işlemleri
        pass

    def sorgula(self):
        # Olay sorgulama işlemleri
        pass

class Sahsiyet:
    def __init__(self, sahsiyet_adi, donemler):
        self.sahsiyet_adi = sahsiyet_adi
        self.donemler = donemler

class Donem:
    def __init__(self, donem_adi, baslangic_tarihi, bitis_tarihi):
        self.donem_adi = donem_adi
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi

# Örnek kullanım
if __name__ == "__main__":
    # Olayların oluşturulması
    olay1 = Olay("Fransız Devrimi", "1789", "Fransa'da monarşinin devrilmesi ve cumhuriyetin ilan edilmesi.")
    olay2 = Olay("Apollo 11 Görevi", "1969", "İnsanlı Ay inişinin gerçekleştirilmesi.")

    # Şahsiyetlerin oluşturulması
    sahsiyet1 = Sahsiyet("Napolyon Bonapart", ["Fransız Devrimi", "Napolyon Savaşları"])
    sahsiyet2 = Sahsiyet("Neil Armstrong", ["Apollo 11 Görevi"])

    # Dönemlerin oluşturulması
    donem1 = Donem("Fransız Devrimi Dönemi", "1789", "1799")
    donem2 = Donem("Uzay Yarışı Dönemi", "1957", "1975")
