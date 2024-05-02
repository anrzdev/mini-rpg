from enemy import Enemy

class Character:
  def __init__(self, name, level, health):
    self.name = name
    self.level = level
    self.health = health
    
  def attack(self, target):
    """Realiza un ataque al objetivo."""
    Enemy.health -= damage
    
  def take_damage(self, damage):
    """Recibe daño."""
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      self.defeated()

  def defeated(self):
    """Maneja la derrota del personaje."""
    print(f"{self.name} ha sido derrotado.")