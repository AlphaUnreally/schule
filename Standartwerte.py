def kasten(name,zeichen = "-", laenge):
    print(zeichen*laenge)
    print(name)
    print(zeichen*laenge)

def kasten2(name, laenge = 10):
    print("-"*laenge)
    print(name)
    print("-"*laenge)

name = input("Name: ")
#a
#laenge = int(input("Wie lang soll das Trennzeichen sein?"))
#print(kasten2(name,laenge))

#b
#print(kasten2(name))
#c.
#print(kasten2(name,2000))