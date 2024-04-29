
class Player:
  def __init__(self,name,level,life,defence,damage,ore):
    self.name = name
    self.level = level
    self.life = life
    self.defence = defence
    self.damage = damage
    self.ore = ore

  def atack(damage):
    if damage > 0:
      totalDamage = damage - defence
      life -= totalDamage