# "Simple" code to make a plot of a function using matplotlib.pyplot

from numpy import *
from matplotlib import pyplot as plt


def plot(func="y = sin(x)", min=-5, max=5, minx=0, maxx=5, miny=0, maxy=10, adax=True, aday=False,
         prec=10):  # Most of these arguments are useless lol

    func = func.replace("^", "**") + " "  # Replace ^ with ** so that python accepts it

    funcf = []
    pas = 0

    for i in range(len(func)):  # Detect all instances of things like 3x and store the positions of them in funcf
        for num in range(10):  # Got tired so time for bad code
            if func[i] == str(num) and (func[i + 1] == "x" or func[i + 1] == "("):
                funcf.append(i)

    for i in funcf:  # Replace things like 3x by 3*x and apply a small correction cuz the length of func changes in every pass of the loop
        pas += 1
        i += pas
        func = func[:i] + "*" + func[i:]

    y = 0
    x = linspace(min, max, int(prec * (abs(min) + abs(max))))

    axis = []

    if adax:  # Why does everything I code looks like spaghetti code
        axis.append(min)
        axis.append(max)
    else:
        axis.append(minx)
        axis.append(maxx)

    if aday:  # I'll probably remove this later
        Y = False
    else:
        Y = True

    exec(
        f"{func}\n"  # Gotta define a loooong string and execute it cuz it seems like python likes to mess with me and force me do that kind of thing lol
        f"plt.plot(x, y)\n"
        f"if Y:\n"
        f"    axis.append(miny)\n"
        f"    axis.append(maxy)\n"
        f"else:\n"
        f"    axis.append(min(y))\n"
        f"    axis.append(max(y))\n"
        f"plt.axis(axis)\n"
        f"plt.grid()\n"
        f"plt.show()")


plot("y = 2x^2 + 1", min = -10, max = 10, miny = 0, maxy = 20, prec = 20)  # Simple example of how you use this
