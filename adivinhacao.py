def jogar():
  print('*   Jogo da Adivinhação   *')
  print('***************************')
  print('***************************')

  secret_number = 42
  max_try = None
  rounds = 1
  points = 1000

  level = input('Escolha um nível de dificuldade entre facil, mediano e dificil \n')
  while((level != 'facil') or (level != 'mediano') or (level != 'dificil')):
    if( level == "facil"):
      max_try = 20
      break
    elif(level == "mediano"):
      max_try = 10
      break
    elif(level == "dificil"):
      max_try = 5
      break
    else:
      print('Você precisa escolher uma dificuldade')
      break

  for rounds in range(1, max_try + 1):
    print('Tentativa {} de {}'.format(rounds, max_try))
    kick = int(input("Digite um número: \n"))
    print('Você digitou: ', kick)

    sucess = kick == secret_number
    biggest = kick > secret_number
    lowest = kick < secret_number

    if (sucess):
      print("Está correto!")
      break
    elif(biggest):
      print("Você errou! O seu chute foi maior que o número secreto")
    elif(lowest):
      print("Você errou! O seu chute foi menor que o número secreto")
    points = abs(points - abs(kick - secret_number))

  print('Fim de jogo')
  print('Sua pontuação foi de ', points)