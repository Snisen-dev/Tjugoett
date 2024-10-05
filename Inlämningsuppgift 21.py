#Inlämningsuppgift 21
import Kortlek as kl

"""Koden nedan körs endast om det den här filen körs
och inte om filen importeras som modul
"""
if __name__ == "__main__":
    """Med hjälp av __innit__ skapas en deck när en variabel skapas
    i klassen Deck"""
    deck = kl.Deck()
    #Metoden Blanda kort körs med listan deck
    kl.Deck.blanda_kort(deck) 
    #Kör spelet 21 med en blandad kortlek (deck)
    kl.Deck.spela_tjugoett(deck)
    
 