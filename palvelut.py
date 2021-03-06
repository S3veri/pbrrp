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
            self.nimi = uusinimi
    def set_ika(self, uusiika):
        if uusiika == False:
            raise ValueError("Anna toinen ika!")
        if  uusiika == True:
            self.ika = uusiika

    def get_asiakasnumero(self):
        """Palautetaan asiakasnumero
        """
        return f'{self.__asiakasnumero[0]:02}-{self.__asiakasnumero[1]:03}-{self.__asiakasnumero[2]:03}'


class Palvelu:
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []
        
    def lisaa_asiakas(self, asiakas):
        if bool(asiakas):
            self.__asiakkaat.append(asiakas)
        else:
            raise ValueError("Anna toinen asiakas")
        
        
        
    def poista_asiakas(self, asiakas):
        try:
            self.asiakkaat.remove(asiakas)
        except ValueError:
            pass
    def tulosta_asiakkaat(self):
        # Alla oleva print ei jostain syystä toimi, muuten ok
        #print("Tuotteen " + self.tuotenimi +  " asiakkaat ovat:")
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))
        print()
    
    def _luo_asiakasrivi(self, asiakas):
        """Palauttaa tiedot asiakkaan nimi, asiakasnumero ja ika.
        """
        return f'{Asiakas.get_nimi(asiakas)} ({Asiakas.get_asiakasnumero(asiakas)}) on {Asiakas.get_ika(asiakas)}-vuotias.'

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
        print("Tuotteen " + self.tuotenimi + " edut ovat")
        for etu in self.__edut:
            print(f'{etu}')
    


