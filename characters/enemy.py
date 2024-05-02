class Enemy:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def attack(self, target):
    """Realiza un ataque al objetivo."""
    pass  # Implementa la lógica de ataque aquí

  def take_damage(self, damage):
    """Recibe daño."""
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      self.defeated()

  def defeated(self):
    """Maneja la derrota del enemigo."""
    print(f"{self.name} ha sido derrotado.")