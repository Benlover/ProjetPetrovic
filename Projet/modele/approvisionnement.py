from datetime import datetime
from random import randint
from modele.station import Station

class Approvisionnement:
    id :int
    capacite_Gazoline: int
    capacite_diesel:int
    date_app: datetime

#    ID, Station, quantité gallon Diesel, Quantité gallon Gazoline, date app.
    def __init__(self, capacite_Gazoline: int = 0 , capacite_diesel:int = 0):
        self.id = randint(1,100)
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel
        self.date_app = datetime.now()
       


