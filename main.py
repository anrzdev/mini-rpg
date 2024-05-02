# Importar la clase Player
from characters.player import Player
from utils.events import explores

getname = input("ingrese su nombre ")
action = ''
ore = 0
actualDef = 3
actualDmg = 2
# Crear una instancia de Player
player = Player(getname, 1, 100, actualDef, actualDmg, 0)


while player.life > 0:
  print(player.name)
  print('nivel ' + str(player.level))
  print('vida ' + str(player.health))
  print('daño ' + str(player.damage))
  action = input("que accion dese realisar")
  explores(action)