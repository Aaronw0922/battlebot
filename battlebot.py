import random



class battlebot:

  def __init__(self,name):
    self.name = name
    self.health = 100
    self.armour = 10.0
    self.damage = 10.0
    self.speed = 10.0

  def alive(self):
    if self.health < 0:
      return False
    else:
      return True

  def attack(self,opponent):
    damage = self.damage - (self.damage * opponent.armour / 100)
    opponent.takedamage(damage)

  def takedamage(self,damage):
    self.health = self.health - damage

  def buildattack(self):
    self.damage = self.damage + 2
    self.speed = self.speed - 1
    self.armour = self.armour - 1

  def buildspeed(self):
    self.damage = self.damage - 1
    self.speed = self.speed + 2
    self.armour = self.armour - 1

  def buildarmour(self):
    self.damage = self.damage - 1
    self.speed = self.speed - 1
    self.armour = self.armour + 2

  def getter(self):
    print(self.name)
    print("health " + str(self.health))
    print("speed " + str(self.speed))
    print("damage " + str(self.damage))
    print("armour " + str(self.armour))

  def action(self,opponent):
    num = random.randint(0,100)
    if num <= 10:
      self.buildattack()
      print(self.name + " built his attack damage")
    elif num <= 20:
      self.buildspeed()
      print(self.name + " built his speed")
    elif num <= 30:
      self.buildarmour()
      print(self.name + " built his armour")
    elif num <= 90:
      self.attack(opponent)
      print(self.name + " attacked you")
    else:
      print(self.name + "blew up")
