pierre = -1
feuille = 0
ciseau = 3

winpierre = pierre + ciseau #2
winfeuille = feuille + pierre #-1
winciseau = ciseau + feuille #3



def play(n):
    print("touches du joueur 1: Q S D \ntouches du joueur 2: K L M")
    point1 = 0
    point2 = 0
    for i in range(n):
        str = input("\nq/k = pierre, s/l = feuille, d/m = ciseau")
        if str[0] == "q" or str[1] == "q":
            p1 = pierre
        elif str[0] == "s" or str[1] == "s":
            p1 = feuille
        elif str[0] == "d" or str[1] == "d":
            p1 = ciseau

        if str[0] == "k" or str[1] == "k":
            p2 = pierre
        elif str[0] == "l" or str[1] == "l":
            p2 = feuille
        elif str[0] == "m" or str[1] == "m":
            p2 = ciseau


        if p1 + p2 == winpierre:
            if p1 == pierre:
                point1 += 1
                print("Le joueur 1 gagne")
            elif p2 == pierre:
                point2 += 1
                print("Le joueur 2 gagne")
        elif p1 + p2 == winfeuille:
            if p1 == feuille:
                point1 += 1
                print("Le joueur 1 gagne")
            elif p2 == feuille:
                point2 += 1
                print("Le joueur 2 gagne")
        elif p1 + p2 == winciseau:
            if p1 == ciseau:
                point1 += 1
                print("Le joueur 1 gagne")
            elif p2 == ciseau:
                point2 += 1
                print("Le joueur 2 gagne")
        else:
            print("Personne ne gagne")
        print(f"{point1}-{point2}")