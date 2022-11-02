print("\It is VIP room!")

reiting = 0
sec = 0
nic = ""
while not nic:
  nic = input("Name: ")
pashord = ""
while not pashord:
  pashord = input("Pashord:")

if nic == "Red" and pashord == "321":
  print("Hello Red!")
  sec = 2
  reiting = 2
  print("Your reiting is: ", reiting)

elif nic == "Green" and pashord == "123":
  print("Hello Green!")
  sec = 2
  reiting = 1
  print("Your reiting is: ", reiting)

else:
  print("We can't find this ACC")