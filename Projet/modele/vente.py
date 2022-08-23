from datetime import datetime
from random import randint

class Vente:
    IdVente : int
    capacite_Gazoline: int
    capacite_diesel:int
    dateVente : datetime

    
    def __init__(self,capacite_Gazoline: int = 0,capacite_diesel:int = 0):
        self.IdVente = randint(1,100)
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel
        self.dateVente = datetime.now()
    
