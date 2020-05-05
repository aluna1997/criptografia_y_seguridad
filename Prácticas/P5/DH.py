from random import randint

class Participant():


    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.p = p
        self.g = g
        self.participant = participant
        self.s = self.seed()

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        self.aleatorio = randint(1,(self.p - 1) % self.p)
        return (self.g ** self.aleatorio) % self.p
        

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """

        s = (self.participant.s ** self.aleatorio) % self.p