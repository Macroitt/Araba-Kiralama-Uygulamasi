# Ba�l� listedeki her bir eleman� temsil eder
class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None

# D���mleri bir araya getirerek bir liste olu�turur
class BagliListe:
    def __init__(self):
        self.bas = None

    def ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:# E�er liste bo�sa, yeni d���m ba� olur
            self.bas = yeni_dugum
        else:# Liste bo� de�ilse, listenin sonuna ekleme yap�l�r
            mevcut = self.bas
            while mevcut.sonraki:# Son d���m bulunur
                mevcut = mevcut.sonraki
            mevcut.sonraki = yeni_dugum

    def listele(self):
        mevcut = self.bas
        while mevcut:
            print(mevcut.veri)
            mevcut = mevcut.sonraki

# Arabalar� bir ikili arama a�ac� olarak saklar
class AracAgaci:
    def __init__(self, marka, model, yil, fiyat):
        self.marka = marka #Ebeveyn
        self.model = model #�ocuk 1
        self.yil = yil #�ocuk 2
        self.fiyat = fiyat
        self.sol = None
        self.sag = None

    def ekle(self, yeni_marka, yeni_model, yeni_yil, yeni_fiyat):
        if yeni_marka < self.marka:# Yeni marka alfabetik olarak daha k���kse sol tarafa eklenir
            if self.sol is None:
                self.sol = AracAgaci(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
            else:
                self.sol.ekle(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
        else:# B�y�kse sa� tarafa eklenir
            if self.sag is None:
                self.sag = AracAgaci(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
            else:
                self.sag.ekle(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)

 # A�ac� s�ral� �ekilde listeler
    def listele(self):
        if self.sol:
            self.sol.listele()
        print(f"{self.marka} {self.model} {self.yil} - {self.fiyat} TL")
        if self.sag:
            self.sag.listele()

    def kirala(self, marka, model):
        if self.marka == marka and self.model == model:
            return None  # Kiralanan ara� a�a�tan silinir
        elif self.sol and marka < self.marka:
            self.sol = self.sol.kirala(marka, model)
        elif self.sag and marka >= self.marka:
            self.sag = self.sag.kirala(marka, model)
        return self  # Ana d���m korunur

# Rezervasyonlar i�in FIFO (First-In-First-Out) veri yap�s� (F�r�n s�ras�na ilk giren ilk ��kar)
class Kuyruk:
    def __init__(self):
        self.elemanlar = [] # Kuyruk elemanlar�n� liste olarak tutar

    def ekle(self, veri):
        self.elemanlar.append(veri)

    #�lk eleman� ��kar�r
    def cikar(self):
        if not self.bos_mu():
            return self.elemanlar.pop(0)
        return None

    def bos_mu(self):
        return len(self.elemanlar) == 0

    def listele(self):
        for eleman in self.elemanlar:
            print(eleman)

if __name__ == "__main__":
    arac_agaci = AracAgaci("Toyota", "Corolla", 2016, 600)
    arac_agaci.ekle("Toyota", "Camry", 2021, 600)
    arac_agaci.ekle("Toyota", "Yaris", 2019, 450)
    arac_agaci.ekle("Honda", "Civic", 2021, 550)
    arac_agaci.ekle("Honda", "Accord", 2020, 580)
    arac_agaci.ekle("Honda", "Jazz", 2018, 400)
    arac_agaci.ekle("Ford", "Fiesta", 2019, 450)
    arac_agaci.ekle("Ford", "Focus", 2020, 500)
    arac_agaci.ekle("Ford", "Mustang", 2021, 700)
    arac_agaci.ekle("BMW", "320i", 2020, 800)
    arac_agaci.ekle("BMW", "X5", 2019, 900)
    arac_agaci.ekle("BMW", "i3", 2021, 850)
    arac_agaci.ekle("Mercedes", "C-Class", 2020, 850)
    arac_agaci.ekle("Mercedes", "E-Class", 2019, 1000)
    arac_agaci.ekle("Mercedes", "A-Class", 2021, 750)
    arac_agaci.ekle("Volkswagen", "Golf", 2020, 550)
    arac_agaci.ekle("Volkswagen", "Passat", 2024, 800)
    arac_agaci.ekle("Volkswagen", "Polo", 2021, 500)
    arac_agaci.ekle("Audi", "A4", 2020, 800)
    arac_agaci.ekle("Audi", "Q5", 2023, 1000)
    arac_agaci.ekle("Audi", "A3", 2019, 700)
    arac_agaci.ekle("Hyundai", "Elantra", 2020, 400)
    arac_agaci.ekle("Hyundai", "Tucson", 2021, 500)
    arac_agaci.ekle("Hyundai", "Accent", 2019, 350)
    arac_agaci.ekle("Nissan", "Altima", 2020, 550)
    arac_agaci.ekle("Nissan", "Sentra", 2021, 500)
    arac_agaci.ekle("Nissan", "Maxima", 2019, 600)

    rezervasyonlar = Kuyruk() # Rezervasyonlar i�in kuyruk olu�turulur
    kiralanan_araclar = BagliListe() # Kiralanan ara�lar i�in ba�l� liste olu�turulur

    while True:
        print("\n1. Ara� Ekle\n2. Rezervasyon Ekle\n3. Ara� Kirala\n4. Ara�lar� Listele\n5. Kiralanan Ara�lar� Listele\n6. Rezervasyonlar� Listele\n7. ��k��")
        secim = input("Bir se�enek girin: ")

        if secim == "1":
            marka = input("Ara� markas�n� girin: ")
            model = input("Ara� modelini girin: ")
            yil = int(input("Ara� y�l�n� girin: "))
            fiyat = int(input("Ara� fiyat�n� girin: "))
            arac_agaci.ekle(marka, model, yil, fiyat)
            print("Ara� ba�ar�yla eklendi!\n")
        elif secim == "2":
            musteri = input("Rezervasyon yapan ki�inin ad�n� girin: ")
            rezervasyonlar.ekle(musteri)
            print("Rezervasyon ba�ar�yla eklendi!\n")
        elif secim == "3":
            if rezervasyonlar.bos_mu():
                print("Bekleyen rezervasyon bulunmamaktad�r.\n")
            else:
                musteri = rezervasyonlar.cikar()
                marka = input("Kiralanacak arac�n markas�n� girin: ")
                model = input("Kiralanacak arac�n modelini girin: ")
                gun = int(input("Ka� g�nl���ne kiralanacak: "))
                arac_agaci = arac_agaci.kirala(marka, model)
                kiralanan_araclar.ekle(f"{musteri} - {marka} {model} ({gun} g�n)\n")
                print(f"{musteri} i�in ara� kiraland�: {marka} {model} ({gun} g�n)\n")
        elif secim == "4":
            print("Mevcut ara�lar:\n")
            arac_agaci.listele()
        elif secim == "5":
            print("Kiralanan ara�lar:\n")
            kiralanan_araclar.listele()
        elif secim == "6":
            print("Bekleyen rezervasyonlar:\n")
            rezervasyonlar.listele()
        elif secim == "7":
            print("��k�� yap�l�yor...")
            break
        else:
            print("Ge�ersiz se�enek, tekrar deneyin.\n")
