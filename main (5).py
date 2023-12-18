############### Blackjack Project #####################
############### Our Blackjack House Rules #####################
## El mazo es de tamaño ilimitado.
## No hay comodines.
## El Jack/Queen/King cuentan todos como 10.
## El As puede contar como 11 o 1.
## Usar la siguiente lista como mazo de cartas:
## Las cartas en la lista tienen igual probabilidad de ser dibujadas.
## Las cartas no se eliminan del mazo al ser dibujadas.
## La computadora es el Dealer.

## DECLARACIONES ##
import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Continua = True
Deal = True
sigue = True

## FUNCIONES ##
def deal_card():
  Deck = random.choice(cards)
  return Deck
def AZ():
  if sum(user_cards) > 21 and 11 in user_cards:
    user_cards.remove(11)
    user_cards.append(1)
    print("Parece que nos pasamos pero contaremos el Az como 1")
    print(f"Tus cartas: {user_cards}, score: {sum(user_cards)}")
    print(" ")
def AZ_PC():
  if sum(computer_cards) > 21 and 11 in computer_cards:
    computer_cards.remove(11)
    computer_cards.append(1)

def Score():
  print(f"Tus cartas: {user_cards}, score: {sum(user_cards)}")
  print(f"Cartas de la computadora:{computer_cards},  score: {sum(computer_cards)}")
  
def Ganador_1():
  if sum(user_cards) == 21 and sum(computer_cards) < sum(user_cards):
    print("Blackjack! Ganaste!")
  elif sum(computer_cards) == 21 and sum(computer_cards) > sum(user_cards):
    print("La computadora tiene Blackjack! Perdiste!")
  elif sum(computer_cards) > 21:
    print("La computadora se paso! Ganaste!")
  elif sum(user_cards) == sum(computer_cards):
    print("Empate! Nadie gana!")
  elif sum(user_cards) > sum(computer_cards):
    print("Ganaste!")
  else:
    print("Perdiste!")
  
## LOGO ##
while Continua is True:
  Game = input("Quieres jugar BlackJack? teclea 'y' para jugar o 'n' para salir: ").lower()
  if Game == "y":
    print(logo)
    print("\n")
    ## JUEGO ##
    user_cards = []
    computer_cards = []
    ## ETAPA 1 ## ACA SE DAN LAS CARTAS AL USUARIO Y AL COMPUTADOR ##
    for _x in range(1,3):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    print(f"Tus cartas: {user_cards}, score: {sum(user_cards)}")
    print(f"Primera carta de la computadora: {computer_cards[0]}")
    ## ETAPA 2 ## ACA SE PREGUNTA SI EL USUARIO QUIERE OTRA CARTA ##
    while Deal is True:
      # CONVIERTES LOS AZ EN 1 SI SE PASA DE 21 #
      AZ()
      AZ_PC()
      if sum(user_cards) > 21:
        print("Te pasaste! Perdiste!")
        break
      Deal_again = input("Quieres otra carta? teclea 'y' para 'n' para no: ").lower()
      if Deal_again == "y":
            user_cards.append(deal_card())
            print(f"Tus cartas: {user_cards}, score: {sum(user_cards)}")
            print(f"Primera carta de la computadora: {computer_cards[0]}")
            print(" ")
      ## ETAPA 3 ## ACA EL USUARIO SE MANTIENE Y LA COMPUTADORA JUEGA ##
      elif Deal_again == "n":
        while sum(user_cards) > sum(computer_cards) or sum(computer_cards) == sum(user_cards) and sum(computer_cards) < 21 :
              computer_cards.append(deal_card())
        print(" ")
        Score()
        print(" ")
        Ganador_1()
        print(" ")
        break
  ## ETAPA 4 ## ACA SE PREGUNTA SI
###############################################################################################              
  elif Game == "n":
    print("Hasta luego!!")
    Continua = False
  else:
    clear()
    print("Respuesta invalidad, vuelve a intentarlo")
    

