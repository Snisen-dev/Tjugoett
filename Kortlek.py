import random
import pyinputplus as pyip


#Här är en klass som beskriver kort
class Kort:
    
    #När klassen anropas skapas automatiskt ett kort med färg och valör
    def __init__(self, valor:str, farg:str):
        self.valor = valor
        self.farg = farg

    #När ett objekt i klassen anropas skrivs objektet ut som en sträng
    #Med Färgen först följt av valören
    def __repr__(self):
        return f"{self.farg} {self.valor}"
        
#Här är en klass som beskriver kortleken
class Deck:
    #Definiera kortleken
    def __init__(self):
        self.farg:list = ["Hjärter", "Ruter", "Spader", "Klöver"]  #Lista på färger
        self.valor:list = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung"] #Lista på Valörer
        #Kortleken skapas genom att köra en loop som tar fram alla kombinerar av elementen i dom 2 listorna
        #Samt varje nytt element i Self.nydeck är av klassen Kort
        self.ny_deck:list = [Kort(valor, farg) 
                        for farg in self.farg 
                        for valor in self.valor
                        ]  
        
    def dela_kort(self):
        #Kollar om det är färre än 10 kort och anropar då blanda kort
        if len(self.ny_deck) < 10:
            print("Blandar om Kortleken.")
            self.blanda_kort()

        #Tar ut översta kortet i korleken, tar även bort det kortet så det inte kan fås igen
        return self.ny_deck.pop() 
    
    #En funktion för att blanda kort
    def blanda_kort(self):
        #ser till att inte blanda korten om kortleken är ko
        if len (self.ny_deck)<52:
            self.ny_deck=Deck().ny_deck
        
        #Här blandas leken
        random.shuffle(self.ny_deck) 
        #Här kuperas leken, (onödigt men tänkte att det var kul)
        for i in range(3):
            slumptal = random.randint(10, 42)
            del_1 = self.ny_deck[:slumptal]
            del_2 = self.ny_deck[slumptal:]
            self.ny_deck = del_2 + del_1
            #Hade planerat att lägga in ASCII bilder men dom blev inge snygga
        return self.ny_deck

    #Här är en metod för att definiera handens valör
    #Den kommer anropas för både spelaren och huset händer
    def hand_tot_valor(self,hand:list):
        #Här skapas 2 lokala variabler i funktionen
        total:int = 0
        antal_ess:int = 0

        #En loop som kör antal gånger som du har kort i handen
        #Då varje kort i handen är av klassen Kort så kan .valor anropas
        for kort in hand:
            if kort.valor == "Knekt":
                total += 11  
            elif kort.valor == "Dam":
                total += 12
            elif kort.valor == "Kung":
                total += 13
            elif kort.valor == "Ess":
                antal_ess += 1  # Hantera ess senare
                total += 14  # Vi antar att ess är 11 till att börja med
            else:
                # Övriga kort som endast har ett nummer lägs bara till som det nummeret
                total += int(kort.valor)

        # Om totalen överstiger 21 och vi har ess, omvärdera ess till 1
        while total > 21 and antal_ess > 0:
            total -= 13
            antal_ess -= 1

        return total

    #Metod för att spela 21
    def spela_tjugoett(self):
        #Frågar först om man vill spela Ja/Nej. OM nej avsluts metoden
        spela=pyip.inputYesNo(prompt="Nu ska vi köra svenska verisionen av Tjugoett.\n"
                              "Vill du köra? Ja/Nej\n",yesVal="Ja",noVal="Nej").lower()
        if spela=="nej":
            return
        #2 tomma listor för spelarens och husets hand
        hand:list=[]
        husets_hand:list=[]
        
        while True:
        #En loop för hela spelet 

            while True:
            #En loop för spelaren

                #En variabel för varje nytt kort
                nytt_kort:Kort = self.dela_kort()
                
                print(f"Du fick: {nytt_kort}")
                #Lägger till kortet i en hand variabeln
                hand.append(nytt_kort)

                #Här anropas valör metoden som har koll på totala valören och skapar en ny variabel total_valör
                total_valor = self.hand_tot_valor(hand)
                print(f"Din totala valör: {total_valor}")

                #Om handens valör är större än 21 blir spelaren tjock
                if total_valor > 21:
                    print("Du blev tjock!")
                    #Spelaren får frågan om hen ska spela igen
                    spela = pyip.inputYesNo(prompt="Vill du fortsätta köra? Ja/Nej \n", yesVal="Ja", noVal="Nej").lower()
                    if spela == "nej":
                        return
                    else:
                        hand = []  #Om spelaren vill spela måste handen nollställas
                        
                #Om spelaren fick 21 får huset börja köra
                elif total_valor == 21:
                    print("Du har 21, Huset börjar köra")
                    break
                else:
                    #Nedan är om spelaren har mindre än 21 och blir då frågad om hen vill ha ett till kort,
                    #Om spelaren säger nej får huset köra
                    svar = pyip.inputYesNo(prompt="Vill du ha ett till kort? Ja/Nej\n", yesVal="Ja", noVal="Nej").lower()
                    if svar == "nej":
                        print("Du stannar. Dags för huset att köra.")
                        break
        
        
            while True:
            #En loop för huset, denna är snarlik spelarens loop men skiljer sig vid if satsen
            
                husets_nya_kort = self.dela_kort()
                print(f"Huset fick: {husets_nya_kort}")
                husets_hand.append(husets_nya_kort)
                

                husets_totala_valor = self.hand_tot_valor(husets_hand)
                print(f"Husets totala valör: {husets_totala_valor}")
                #Här blir huset tjock
                if husets_totala_valor > 21:
                    print("Huset blev tjockt! Du vann.")
                    break
                #Här vinner huset om dess hand har samma valör som spelarens
                elif husets_totala_valor == total_valor:
                    print("Oavgjort! Huset vinner handen.")
                    break
                #Här vinner huset om dess hand är större än spelarens
                elif husets_totala_valor > total_valor:
                    print("Huset vann handen!")
                    break
                #Här stannar huset har 17 eller större valör och spelaren vinner
                elif husets_totala_valor >= 17:  
                    print("Huset stannar. Du vann handen!")
                    break
                
            #Här blir spelaren frågad om hen vill fortsätta att köra efter rundans omgång
            fortsätt_spela=pyip.inputYesNo(prompt="Vill fortsätta köra? (Ja/Nej)",yesVal="Ja",noVal="Nej").lower()
            if fortsätt_spela=="nej":
                break
            else:
                hand=[] #Här måste händerna nollställas
                husets_hand=[]
    
