import random

class Asiakas:
    def __luo_nro(self):
        """Muodostaa satunnaisen asiakasnumeron
        :ivar numerolista: lista jossa satunnaisesti generoitu asiakasnumero
        :type numerolista: int[]
        """
        numerolista = []
        numerolista.append(random.randint(0, 99))
        numerolista.append(random.randint(0, 999))
        numerolista.append(random.randint(0, 999))
        return numerolista

    def __init__(self, nimi, ika):
        """Konstruktori, jonka muuttujat peritään
        :ivar asiakasnumero: asiakkaan puhelin numero
        :type asiakasnumero: int[]
        :ivar nimi: asiakkaan nimi
        :type nimi: str
        :ivar ika: asiakkaan ikä
        :type ika: int
        """
        self.__asiakasnumero = self.__luo_nro()
        self.__nimi = str(nimi)
        self.__ika = int(ika)

    def get_nimi(self):
        return self.__nimi
    def get_ika(self):
        return self.__ika
    def set_nimi(self, uusinimi):
        if uusinimi == False:
            raise ValueError("Anna toinen nimi!")
        if uusinimi == True:
            self.__nimi = uusinimi
    def set_ika(self, uusiika):
        if uusiika == False:
            raise ValueError("Anna toinen ika!")
        if  uusiika == True:
            self.__ika = uusiika

class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        self.asiakkaat = []
        
    def lisaa_asiakas(self, Asiakas):
        self.asiakkaat.append(Asiakas)
        if Asiakas == False:
            raise ValueError("Anna toinen asiakas")
        
    def poista_asiakas(self, Asiakas):
        try:
            if Asiakas == False:
                raise ValueError("Anna uusi asiakas")
            else:
                self.asiakkaat.pop(Asiakas)
        except:
            pass
    def tulosta_asiakkaat(self):
            pass
    
    def luo_asiakasrivi(self):
        pass

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(self)
        self.edut = []
    def lisaa_etu(self, Etu):
        self.edut.append(Etu)
        if Etu == False:
            raise ValueError("Anna toinen Etu")
    def poista_etu(self, Etu):
        try:
            if Etu == False:
                raise ValueError("Anna uusi etu")
            else:
                self.edut.pop(Etu)
        except:
            pass
            
    def tulosta_edut(self):
        pass
    pass


