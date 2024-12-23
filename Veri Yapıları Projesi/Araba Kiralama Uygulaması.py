# Baðlý listedeki her bir elemaný temsil eder
class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None

# Düðümleri bir araya getirerek bir liste oluþturur
class BagliListe:
    def __init__(self):
        self.bas = None

    def ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:# Eðer liste boþsa, yeni düðüm baþ olur
            self.bas = yeni_dugum
        else:# Liste boþ deðilse, listenin sonuna ekleme yapýlýr
            mevcut = self.bas
            while mevcut.sonraki:# Son düðüm bulunur
                mevcut = mevcut.sonraki
            mevcut.sonraki = yeni_dugum

    def listele(self):
        mevcut = self.bas
        while mevcut:
            print(mevcut.veri)
            mevcut = mevcut.sonraki

# Arabalarý bir ikili arama aðacý olarak saklar
class AracAgaci:
    def __init__(self, marka, model, yil, fiyat):
        self.marka = marka #Ebeveyn
        self.model = model #Çocuk 1
        self.yil = yil #Çocuk 2
        self.fiyat = fiyat
        self.sol = None
        self.sag = None

    def ekle(self, yeni_marka, yeni_model, yeni_yil, yeni_fiyat):
        if yeni_marka < self.marka:# Yeni marka alfabetik olarak daha küçükse sol tarafa eklenir
            if self.sol is None:
                self.sol = AracAgaci(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
            else:
                self.sol.ekle(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
        else:# Büyükse sað tarafa eklenir
            if self.sag is None:
                self.sag = AracAgaci(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)
            else:
                self.sag.ekle(yeni_marka, yeni_model, yeni_yil, yeni_fiyat)

 # Aðacý sýralý þekilde listeler
    def listele(self):
        if self.sol:
            self.sol.listele()
        print(f"{self.marka} {self.model} {self.yil} - {self.fiyat} TL")
        if self.sag:
            self.sag.listele()

    def kirala(self, marka, model):
        if self.marka == marka and self.model == model:
            return None  # Kiralanan araç aðaçtan silinir
        elif self.sol and marka < self.marka:
            self.sol = self.sol.kirala(marka, model)
        elif self.sag and marka >= self.marka:
            self.sag = self.sag.kirala(marka, model)
        return self  # Ana düðüm korunur

# Rezervasyonlar için FIFO (First-In-First-Out) veri yapýsý (Fýrýn sýrasýna ilk giren ilk çýkar)
class Kuyruk:
    def __init__(self):
        self.elemanlar = [] # Kuyruk elemanlarýný liste olarak tutar

    def ekle(self, veri):
        self.elemanlar.append(veri)

    #Ýlk elemaný çýkarýr
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

    rezervasyonlar = Kuyruk() # Rezervasyonlar için kuyruk oluþturulur
    kiralanan_araclar = BagliListe() # Kiralanan araçlar için baðlý liste oluþturulur

    while True:
        print("\n1. Araç Ekle\n2. Rezervasyon Ekle\n3. Araç Kirala\n4. Araçlarý Listele\n5. Kiralanan Araçlarý Listele\n6. Rezervasyonlarý Listele\n7. Çýkýþ")
        secim = input("Bir seçenek girin: ")

        if secim == "1":
            marka = input("Araç markasýný girin: ")
            model = input("Araç modelini girin: ")
            yil = int(input("Araç yýlýný girin: "))
            fiyat = int(input("Araç fiyatýný girin: "))
            arac_agaci.ekle(marka, model, yil, fiyat)
            print("Araç baþarýyla eklendi!\n")
        elif secim == "2":
            musteri = input("Rezervasyon yapan kiþinin adýný girin: ")
            rezervasyonlar.ekle(musteri)
            print("Rezervasyon baþarýyla eklendi!\n")
        elif secim == "3":
            if rezervasyonlar.bos_mu():
                print("Bekleyen rezervasyon bulunmamaktadýr.\n")
            else:
                musteri = rezervasyonlar.cikar()
                marka = input("Kiralanacak aracýn markasýný girin: ")
                model = input("Kiralanacak aracýn modelini girin: ")
                gun = int(input("Kaç günlüðüne kiralanacak: "))
                arac_agaci = arac_agaci.kirala(marka, model)
                kiralanan_araclar.ekle(f"{musteri} - {marka} {model} ({gun} gün)\n")
                print(f"{musteri} için araç kiralandý: {marka} {model} ({gun} gün)\n")
        elif secim == "4":
            print("Mevcut araçlar:\n")
            arac_agaci.listele()
        elif secim == "5":
            print("Kiralanan araçlar:\n")
            kiralanan_araclar.listele()
        elif secim == "6":
            print("Bekleyen rezervasyonlar:\n")
            rezervasyonlar.listele()
        elif secim == "7":
            print("Çýkýþ yapýlýyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.\n")
