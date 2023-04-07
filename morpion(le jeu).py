from numpy import *

def gengrid(x,y):
    grid = []
    grid.append(y)
    grid.append(x)
    for i in range(x*y):
        grid.append(0)
    affgrid(grid)
    return grid

def affgrid(grid):
    res = ""
    x = grid[0]
    y = grid[1]
    grid = grid[2:]
    for i in range(x*y):
        if grid[i] == 0:
            res += "▢ "
        elif grid[i] == 1:
            res += "X "
        elif grid[i] == -1:
            res += "O "

        if i % y == y-1:
            res += "\n"
    print(res)

def croix(grid, pos):
    if grid[pos+1] == 0:
        grid[pos+1] = 1
        affgrid(grid)
        checkwin(grid)
        return grid

    else:
        print("ya deja quelque chose la")
        affgrid(grid)

def rond(grid, pos):
    if grid[pos+1] == 0:
        grid[pos+1] = -1
        affgrid(grid)
        checkwin(grid)
        return grid
    else:
        print("ya deja quelque chose la")
        affgrid(grid)

def checkwin(grid):
    x = grid[0]
    y = grid[1]
    if x != 3 or y != 3:
        print("je fait des checks pour savoir qui gagne que pour le 3X3")
        affgrid(grid)
    else:
        grid = grid[2:]
        valgrid = 0
        b1 = grid[:3]
        b2 = grid[3:6]
        b3 = grid[6:]
        for i in range(9):
            valgrid += abs(grid[i])

        if b1[0] + b2[0] + b3[0] == 3:
            print("les croix ont gagné")

        elif b1[0] + b2[0] + b3[0] == -3:
            print("les ronds ont gagné")

        elif b1[1] + b2[1] + b3[1] == 3:
            print("les croix ont gagné")

        elif b1[1] + b2[1] + b3[1] == -3:
            print("les ronds ont gagné")

        elif b1[2] + b2[2] + b3[2] == 3:
            print("les croix ont gagné")

        elif b1[2] + b2[2] + b3[2] == -3:
            print("les ronds ont gagné")

        elif b1[0] + b1[1] + b1[2] == 3:
            print("les croix ont gagné")

        elif b1[0] + b1[1] + b1[2] == -3:
            print("les ronds ont gagné")

        elif b2[0] + b2[1] + b2[2] == 3:
            print("les croix ont gagné")

        elif b2[0] + b2[1] + b2[2] == -3:
            print("les ronds ont gagné")

        elif b3[0] + b3[1] + b3[2] == 3:
            print("les croix ont gagné")

        elif b3[0] + b3[1] + b3[2] == -3:
            print("les ronds ont gagné")

        elif b1[0] + b2[1] + b3[2] == 3:
            print("les croix ont gagné")

        elif b1[0] + b2[1] + b3[2] == -3:
            print("les ronds ont gagné")


        elif b1[2] + b2[1] + b3[0] == 3:
            print("les croix ont gagné")

        elif b1[2] + b2[1] + b3[0] == -3:
            print("les ronds ont gagné")

        elif valgrid == 9:
            print("Match nul")





grid = gengrid(3,3)