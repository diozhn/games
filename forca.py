import random

def print_opening_message(game_name):
    print('*********************************')    
    print('***Welcome to the {}!***'.format(game_name))    
    print('*********************************\n')

def load_secret_word():
    archive = open('words.txt', 'r')
    words = []

    for line in archive:
      line = line.strip()
      words.append(line)
    archive.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

    return secret_word

def start_corret_letters(word):
    return ['_' for letter in word]

def get_kick():
    kick = input('Qual a letra? ')
    kick = kick.strip().upper()
    return kick

def corret_kick(kick, corret_letters, secret_word):
  position = 0
  for letter in secret_word:
    if(kick == letter):
      corret_letters[position] = letter
    position += 1

def print_winner_message():
  print('Parabéns, você ganhou!') 
  print("       ___________      ") 
  print("      '._==_==_=_.'     ") 
  print("      .-\\:      /-.    ") 
  print("     | (|:.     |) |    ") 
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ") 
  print("         '::. .'        ") 
  print("           ) (          ") 
  print("         _.' '._        ") 
  print("        '-------'       ")

def print_loser_message(secret_word):
  print('Puxa, você foi enforcado!')
  print('A palavra secreta era {}'.format(secret_word))
  print("    _______________         ")
  print("   /               \        ")
  print("  /                 \       ")
  print("//                   \/\    ")
  print("\|   XXXX     XXXX   | /    ") 
  print(" |   XXXX     XXXX   |/     ") 
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ") 
  print(" \__      XXX      __/      ") 
  print("   |\     XXX     /|        ") 
  print("   | |           | |        ") 
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ") 
  print("   \_             _/        ") 
  print("     \_         _/          ") 
  print("       \_______/            ")

def jogar():
  print_opening_message('Gallows Game')
  secret_word = load_secret_word()
  corret_letters = start_corret_letters(secret_word)
  print(corret_letters)

  hit = False
  hang = False
  errors = 0

  while(not hang and not hit):
    kick = get_kick()
    if(kick in secret_word):
      corret_kick(kick, corret_letters, secret_word)
    else:
        errors += 1
    hang = errors == 6
    hit = '_' not in corret_letters
    print(corret_letters)

  if(hit):
    print_winner_message()
  else:
    print_loser_message(secret_word)
