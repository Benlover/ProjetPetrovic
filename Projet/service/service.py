#IMPORTATION DES MODULES

from typing import ClassVar
from modele.station import Station
from modele.commande import Commande
import logging

class Petrole:
    s_lalue = dict
    s_tabarre = {}
    s_clercine = {}
    s_petionville = {}
    stationGenerale: list= []
    nomStation: str = ''
    capacite_Gazoline: int = 0
    capacite_diesel: int =0 
    station : Station
    diesel: ClassVar[int]
    gazoline: ClassVar[int]
    
    commandes:list =[]

    commande = Commande()


  
    def __init__(self):
          self.s_lalue = dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_clercine= dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_tabarre = dict({
            'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          }) 
          self.s_petionville = dict({
               'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.stationGenerale = []
          station : Station()
          self.commande = []

          
          

    def enregistrerStation(self):
        self.nomStation = Petrole.choixStation(message =' Choisir une station svp !!')
        try:
    
            self.capacite_Gazoline:int = int(input('Saisir la capacité de gazoline !!:'))
        except ValueError as e:
            logging.error(e)      
        try:
             self.capacite_diesel:int = int(input('Saisir la capacité de diesel !! :'))
        except ValueError as e:
            logging.error(e) 

#Verifier si cette station n\'existe pas deja  
#           
        # for listeS in self.stationGenerale:
        #     if listeS.nomStation == self.nomStation:
        #         self.stationGenerale.remove(listeS)
        #         break
        match self.nomStation:
            case 'lalue':
                self.s_lalue.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                
                self.stationGenerale.append(self.s_lalue)
            case 'tabarre':
                self.s_tabarre.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_tabarre)   
            case 'clercine':
                self.s_clercine.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_clercine)  
            case 'Petion-ville':
                self.s_petionville.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_petionville)

        print('Save avec succes') 

       

    def afficherStation(self):
        stat:str = Petrole.choixStation(message='Choisir une station a aficher svp' )

        match stat:

            case 'lalue':
                Petrole.afficher(self.s_lalue)
            case 'tabarre':
                Petrole.afficher(self.s_tabarre)
            case 'clercine':
                Petrole.afficher(self.s_clercine)
            case 'Petion-ville':
                Petrole.afficher(self.s_petionville)
            case default:
                print('Mauvais choix')    

    def afficherStations(self):
        if len(self.stationGenerale)>0:
          for staG in self.stationGenerale:
            print(staG) 
        else:
            print('List empty')    
    @staticmethod         
    def afficher(dicGenerale:dict):
      
             print('***************************************************')
             print(f" \n Station :{dicGenerale.get('nomStation')}"
                   f"\n capacite de stackage de gazoline {dicGenerale.get('capacite_Gazoline')} "
                   f"\n capacité de stockage diesel :{dicGenerale.get('capacite_diesel')}"
                   f"\n Pourcentage de stockage de gazoline :" 
                   f"\n Pourcentage de stockage de diesel : ")   
             print('*************************************************************\n ')


    def ModifierCapacite(self):
        self.nomStation = Petrole.choixStation(message='Choisir une station svp')
        match self.nomStation:
            case 'lalue':
                if len(self.s_lalue)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')

                    #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                    'nomStation': self.nomStation,
                    'capacite_Gazoline':Petrole.gazoline,
                    'capacite_diesel':Petrole.diesel
                     })
                    self.s_lalue.update(self.s_lalue)
                else:
                    print('')
                       
            case 'tabarre':
                if len(self.s_tabarre)>0:
                    Petrole.gazoline= self.s_tabarre.get('capacite_Gazoline')
                    Petrole.diesel = self.s_tabarre.get('capacite_diesel')

                        #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_tabarre.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_tabarre.update(self.s_tabarre)
            case 'clercine':
                if len(self.s_clercine)>0:
                    Petrole.gazoline= self.s_clercine.get('capacite_Gazoline')
                    Petrole.diesel = self.s_clercine.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_clercine.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_clercine.update(self.s_clercine)

            case 'Petion-ville':
                if len(self.s_petionville)>0:
                    Petrole.gazoline= self.s_petionville.get('capacite_Gazoline')
                    Petrole.diesel = self.s_petionville.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_petionville.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_petionville.update(self.s_petionville)
        print('Modifier avec Succes')        
            #   case default:
            #     print('Mauvais Choix ????')

    @staticmethod
    def choose_essence()->str:
        return input('\n a-GAZOLINE'
                     '\n b-DIESEL'
                     '\n c-LES DEUX'
                     '\n d-PRESSER POUR QUITTER'
                     '\n =====>')
           
    

    @staticmethod
    def choixStation( message: str)->str:
        while True:
            station:str = input(f'******{message}********\n'
                                 '\n a- lalue'
                                '\n b-tabarre'
                                '\n c-clercine'
                                '\n d-Petion-ville'
                                '\n ===>:')
            match station.lower():
                        case 'a':
                            return 'lalue'
                        case 'b':
                             return 'tabarre'
                        case 'c':
                            return 'clercine'
                        case 'Petion-ville':
                            return ''
                        case default:
                           print('Mauvais Choix')   
    @staticmethod                       
    def donnes():
        while True:
            Type_essence:str = Petrole.choose_essence()
            match Type_essence:
                case 'a':
                    Petrole.gazoline= int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                case 'b':
                    Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                case 'c':
                   Petrole.gazoline = int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                   Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                
                case default:
                    break


#**************************MODULE COMMANDE ******************
     
    def pourcentage_gazoline_disponible(self):
        pourcentage = 0.0
        for s in self.stationGenerale:
            pourcentage = pourcentage + (100 - s.capacite_Gazoline) 
            return pourcentage /len(self.stationGenerale)

    def pourcentage_diesel_disponible(self):
        pourcentage = 0.0
        for s in self.stationGenerale:
            pourcentage =pourcentage + (100 - s.capacite_diesel) 
            return pourcentage /len(self.stationGenerale)
   
    def quantite_gazoline(self):
        totG = 0 
        if len(self.stationGenerale)>0:
          for s in self.stationGenerale:
             totG = totG + self.capacite_Gazoline
        return totG

    def quantite_diesel(self):
        totG = 0 
        if len(self.stationGenerale)>0:
          for s in self.stationGenerale:
             totG = totG + self.capacite_diesel
        return totG   

#QUANTITE TOTAL ESSENCE POUR UN STATION DONNEE
    def total_essence(self):
        return self.quantite_gazoline + self.quantite_diesel 

#POURCENTAGE TOTAL D'ESSNCE
    
    def pourcentage_total_essence(self,qtediesel_and_gazoline_utilise :float):
        return (qtediesel_and_gazoline_utilise * 100)/ self.total_essence

#METHODE PERMETTANT ENREGISTRER UNE COMMANDE             
    def save_commande(self):
        if len(self.stationGenerale)>0:
            qtediesel_and_gazoline_utilise : float = 0
            for stat in self.stationGenerale:
                qteGazole_ut = stat.quantite_gazoline_utilise()
                qteDiese_ut = stat.quantite_diesel_utilise()
                qtediesel_and_gazoline_utilise += qteGazole_ut + qteDiese_ut
            #Affichage des donnees 
                Petrole.afficher_qte_disponible_and_qte_utilise(self.stationGenerale,qteGazole_ut = qteGazole_ut ,qteDiese_ut = qteDiese_ut)
                pourcentageTotal :float = self.pourcentage_total_essence(qtediesel_and_gazoline_utilise=qtediesel_and_gazoline_utilise) 
            if pourcentageTotal >= 50:
                if self.valide_commande():
                    self.commande = Commande(quantiteGallon_Gazoline = self.quantite_gazoline,quantiteGallon_Diesel = self.quantite_diesel)
                    if self.valide_commande:
                        return True

                    self.commandes.append(Commande)

                    print('')
                else:
                    print('')   

            else:
                print('')
        else:
            print('')
    

    
    @staticmethod
    def afficher_qte_disponible_and_qte_utilise(self,qteGazole_ut : float,qteDiese_ut:float):
        print(f"\n *********************{self.nomStation}***************"
              f"\n  {int(qteGazole_ut)}"
              f"\n {int(qteDiese_ut)}"
              f"\n  {int(self.quantite_gazoline_disponible)}"
              f"\n {int(self.quantite_diesel_disponible)}"
              )
    def afficher_commande(self):
        if len(self.commandes)>0:
          for lisC in self.commandes:
             print(lisC)
        else:
            print('liste vide')
    @staticmethod
    def valide_commande()->True:
           return input ('Voulez-vous effectuer de commande : O pour oui N pour non valider la commande !!!') == 'o'
  
    # def _status(self):
    #     if len(self.commandes)>0:
          

if __name__ == '__main__':    

    Petrole = Petrole()
    Petrole.enregistrerStation()
    Petrole.afficherStations()

