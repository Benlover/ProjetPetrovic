
from datetime import datetime
from random import randint, random


class Commande:
     id :int
     capacite_Gazoline: int
     capacite_diesel: int
     dateCommande: datetime
     etat :str

     def __init__(self,capacite_Gazoline: int= 0,capacite_diesel: int = 0):

          self.id = randint(1,100)
          self.capacite_Gazoline = capacite_Gazoline
          self.capacite_diesel = capacite_diesel
          self.dateCommande = datetime.now()
          self.etat = 'Nouvelle'
