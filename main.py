from battleBot import battlebot

mybot = battlebot("aaron")
opponent = battlebot("opponent")

while mybot.alive() and opponent.alive():
  if mybot.speed > opponent.speed:
    command = input("Enter 1 to attack, enter 2 to build speed, enter 3 to build armour, enter 4 to build damage --> ")
    if command == "1":
      mybot.attack(opponent)
    elif command == "2":
      mybot.buildspeed()
    elif command == "3":
      mybot.buildarmour()
    else:
      mybot.buildattack()
    opponent.action(mybot)
    print("-----   Mybot  -------")
    mybot.getter()
    print("---   Opponent  -----")
    opponent.getter()
    print("----------------------")
  else:
    opponent.action(mybot)
    command = input("Enter 1 to attack, enter 2 to build speed, enter 3 to build armour, enter 4 to build damage --> ")
    if command == "1":
      mybot.attack(opponent)
    elif command == "2":
      mybot.buildspeed()
    elif command == "3":
      mybot.buildarmour()
    else:
      mybot.buildattack()
    print("-----   Mybot  -------")
    mybot.getter()
    print("---   Opponent  -----")
    opponent.getter()
    print("----------------------")
