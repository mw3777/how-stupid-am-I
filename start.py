#Begréissung
print ("hello :)")
name1 = input("What's your name?\n")
print("\nHello " + name1 + "\n\n")

#Waat well en kuken
options = "1. stupidness \n2. intelligence \n"
pick = "pick 1 or 2"
print("Here are the  options: \n" + options)
order = input("Pick 1 or 2:\n")

#Wann intelligence ausgewielt gett
if order == "2": print("2 isn't avaible"); order2 = input("pick 1\n")
else: print("")

#Wann stupidness ausgewielt gett
if order == "1" or order2 == "1":
  print("\nWhrite the name of the person")
else: print("")
  
#Numm vun der Persoun
name = input("")

#waarden
import time
time.sleep(0.5)
print("Wait we're processing")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep (1)

#wann Matti
if name == "matti" or name == "Matti": print ("there isn't any stupidness in Matti")
else: print("")

#Wann Iannis
if name == "Iannis" or name == "iannis": print("this is the stupidest person in earth")
else: print("")

#ferdeg wann Iannis oder Matti
if name == "Iannis" or name == "Iannis" or name == "Matti" or name == "matti": print("Thanks using my pogramm"); quit()

#Wann net Iannis oder Matti

#Zoufall  
else:
  import random
  random = random.randint(1,5)

#Resultat vum Zoufall
if random == 1 or random == 2: print (name + " is the stupidest man on earth")
if random == 3 or random == 4: print (name + " is not so stupid")
if random == 5: print (name + " isn't stupid at all")

#Ferdeg wann net Iannis oder Matti
print("\nThanks using my pogramm")
print(":)")
