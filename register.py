print("\It is VIP room!")

reiting = 0
sec = 0
nic = ""
while not nic:
  nic = input("Name: ")
pashord = ""
while not pashord:
  pashord = input("Pashord:")
if nic == "Anoim" and pashord == "iniciatr":
  print("Hello Anoim!")
  sec = 2
  reiting = 2
  print("Your reiting is: ", reiting)
elif nic == "World" and pashord == "secret":
  print("Hello World!")
  sec = 2
  reiting = 1
  print("Your reiting is: ", reiting)
elif nic == "FF" and pashord == "some":
  print("Hello FF!")
  sec = 4
  reiting = 4
  print("Your reiting is: ", reiting)
elif nic == "Mr.J" and pashord == "Nowhere":
  print("Good Morning Mr.J!")
  sec = 5
  reiting = 5
  print("Your reiting is: ", reiting)
elif nic == "guest" or pashord == "guest":
  print("This is guest ACC.")
  sec = 0
  reiting = 0
  print("Your reiting is: ", reiting)
else:
  print("We can't find this ACC")
