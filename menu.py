import adivinhacao
import forca

print('*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")
change = int(input("Qual jogo quer jogar? Digite o número"))

if(change == 1):
  adivinhacao.jogar()
elif(change == 2):
  forca.jogar()