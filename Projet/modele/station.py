


class Station:
    nomStation: str
    capacite_Gazoline: int
    capacite_diesel:int
    pourcentageGazoline : float
    pourcentageDiesel : float

    def __init__(self, nomStation: str = '', capacite_Gazoline: int = 0,capacite_diesel: int = 0,pourcentageGazoline : float = 0.0,pourcentageDiesel : float = 0.0):
        self.nomStation = nomStation
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel
        self.pourcentageGazoline = 0.0
        self.pourcentageDiesel = 0.0

    # if capacite_diesel > 0:
    #      self.pourcentage(qte_vendue =self.capacite_Gazoline, essence = 'gazoline')
    # else:
    #     print('')


    #QANTITE GAZOLINE UTILISE
    def quantite_gazoline_utilise(self)->int:
        
        return (self.capacite_Gazoline * self.capacite_Gazoline)/100

    #QANTITE GAZOLINE UTILISE
    def quantite_diesel_utilise(self)->int:
       return (self.capacite_diesel * self.pourcentageDiesel)/100

    #QUANTITE GALLON DIESEL DISPONIBLE
    def quantite_diesel_disponible(self,qte_vendue: float)->int:
        return self.capacite_diesel - qte_vendue

    #QUANTITE GALLON GAZOLINE DISPONBLE
    def quantite_gazoline_disponible(self,qte_vendue: float)->int:
        return self.capacite_Gazoline - qte_vendue
    


    # def pourcentage(self,qte_vendue:float)->float:
    #     match essence:
    #         case 'gazoline':
    #             self.capacite_Gazoline = (qte_vendue * 100) /self.capacite_Gazoline
    #         case 'diesel':
    #             self.capacite_diesel = (qte_vendue * 100) /self.capacite_diesel
    #         case default:
    #             print('')     

   
        
                    
