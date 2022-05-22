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
        self.__nimi = nimi
        self.__ika = ika

    # Alla esitetty printtaa on vain omaa testausta varten; tämä siis otetaan lopullisesta versiosta pois
    def printtaa(self):
        print(self.__nimi)
        print(self.__ika)
        print(self.__asiakasnumero)

class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        asiakkaat = []
        
    def lisaa_asiakas(Asiakas):
        self.asiakkaat.append(Asiakas)
        if Asiakas == False:
            raise ValueError("Anna toinen asiakas")
        
    def poista_asiakas(Asiakas):
        self.asiakkaat.pop(Asiakas)
        if Asiakas == False:

    def tulosta_asiakkaat():
        for x in range(asiakkaat):
            
            
        pass
    
    def luo_asiakasrivi():
        merkkijono = 
        return 
        pass

class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        edut = []
    def lisaa_etu(Etu):
        self.edut.append(Etu)
        if Etu == False:
            raise ValueError("Anna toinen Etu")
    def poista_etu(Etu):
        self.edut.pop(Etu)
        if Etu == False:
            pass
    def tulosta_edut():
        pass
    pass


# Alla esitetty on testaa yllä mainitut
koe = Asiakas('Ville', 12)
koe.printtaa()

