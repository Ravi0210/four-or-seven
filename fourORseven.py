
money = int(100)
schuld = int(0)
print("Uw portemonnee bevat " + str(money))
print("U heeft " + str(schuld) + " euro aan schulden")

def dobbel2(money, schuld):
    if money < 99:
        money = money + 200
        schuld = schuld + 200
        print("uw geld is op! hier pak dit briefje van 200 aan, schuld: " + str(schuld))
        dobbel2(money, schuld)
    elif schuld > 599 and money > 100:
        schuld = schuld - 600
        print("de deurwaarders hebben uw tv en hifi apperatuur meegenomen! U heeft geen schulden meer")
        print("Uw portemonnee bevat " + str(money))
        dobbel2(money , schuld)
    else:
        import random
        ogen = str((random.randint(1, 6)))
        ogen2 = str((random.randint(1, 6)))
        totaal = int(ogen) + int(ogen2)
        print("u gooide in totaal: " + str(totaal))
        int(totaal)
        if totaal == 4:
            money = money + 30
            print("U WINT!")
            print("u heeft nu " + str(money))
            antwoord = input()
            if antwoord == "gooi":
                dobbel2(money, schuld)
                print(money)
            else:
                dobbel2(money, schuld)
        elif totaal == 7:
            money = money + 30
            print("U WINT! U heeft nu " + str(money))
            antwoord = input()
            if antwoord == "gooi":
                dobbel2(money, schuld)
                print(money)
            else:
                dobbel2(money, schuld)
        else:
            money = money - 100
            print("u verliest probeer het nog een keer!")
            print("u heeft nu " + str(money))
            antwoord = input()
            if antwoord == "gooi":
                dobbel2(money, schuld)
                print(money)
            else:
                dobbel2(money, schuld)

def fourORseven():
    antwoord = input()
    if antwoord == "gooi":
        dobbel2(money, schuld)
    elif antwoord == "help":
        print("u gooit 2 dobbelstenen en daarvan moeten ze in totaal 11 maken dan wordt uw geld verdubbelt gooit u iets anders dan gaat er 5 euro van af")
        fourORseven()
    else:
        print("er ging iets fout probeer het opnieuw!")
        fourORseven()
def startvraag():
    print("u speelt four or seven type 'gooi' om te beginnen of 'help' voor de spelregels ")

startvraag()
fourORseven()
