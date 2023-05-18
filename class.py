class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__yapilan_satislar = {}

    def magaza_satis_tutari(self):
        toplam_satis_tutari = 0
        for satis_zamani, tutar in self.__yapilan_satislar.items():
            toplam_satis_tutari += tutar
        return toplam_satis_tutari

    def satis_kayitlari(self, satis_zamani, tutar):
        self.__yapilan_satislar[satis_zamani] = tutar

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
        
    def get_satici_cinsi(self):
        return self.__satici_cinsi
    
    def satici_satis_tutari(self):
        toplam_satis_tutari = 0
        for satis_zamani, tutar in self.__yapilan_satislar.items():
            toplam_satis_tutari += tutar
        return toplam_satis_tutari

def main():
    magazalar = {}
    while True:
        magaza_adi = input("Mağazanın Adı : ")
        satici_adi = input("Satıcının Adı : ")
        satici_cinsi = input("Satıcı Cinsi : ")
        satis_zamani = input("Satışın Yapıldığı Zaman Dilimi :(GG-AA-YY): ")
        tutar = float(input("Satışın Tutarı : "))


        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = Magaza(magaza_adi, satici_adi, satici_cinsi)

        magazalar[magaza_adi].satis_kayitlari(satis_zamani, tutar)

        devam = input("Farklı Satış Bilgisi Girmek İçin 'e'ye Basın, Çıkmak İçin 'h'ye Basın (e/h): ")
        if devam.lower() != "e":
            break

    for magaza_adi, magaza in magazalar.items():
        print(f"{magaza_adi}:")
        print(f"\t{magaza.get_satici_adi()} Adlı Satıcının Yaptığı Satış Tutarı : {magaza.satici_satis_tutari()}")
        print(f"\tToplam Satış Tutarı : {magaza.magaza_satis_tutari()}")



if __name__ == "__main__":
    main()
