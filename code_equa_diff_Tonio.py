import numpy as np
import matplotlib.pyplot as plt

#   Données

alpha = 10
beta = 2
gamma = 10
delta = 2

#   Fonctions préalables

def prey(x1, x2):
    global alpha, beta
    return x1*(alpha - beta*x2)

def predator(x1, x2):
    global gamma, delta
    return -x2*(gamma - delta*x1)

#   Question 2

xMin, xMax = (0, 10)
yMin, yMax = (0, 10)
N = 40 # Nombre de points par ligne/colonne
listeX = np.linspace(xMin, xMax, N)
listeY = np.linspace(yMin, yMax, N)

gridX, gridY = np.meshgrid(listeX, listeY)

gridXp = prey(gridX, gridY)
gridYp = predator(gridX, gridY)

plt.figure("Champ de vecteur 1")
plt.quiver(gridX, gridY, gridXp, gridYp, color = 'r')
plt.show()

plt.figure("Champ de vecteur 2")
plt.streamplot(gridX, gridY, gridXp, gridYp, color = 'r')
plt.show()

#   Question 5

def H(x1, x2):
    return delta*x1 - gamma*np.log(x1) + beta*x2 - alpha*np.log(x2)

def display_contour(f, x, y, levels):
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig, ax = plt.subplots()
    contour_set = plt.contour(
        X, Y, Z, colors="blue", linestyles="dashed", 
        levels=levels 
    )
    ax.clabel(contour_set)
    plt.grid(True)
    plt.xlabel("$x_1$") 
    plt.ylabel("$x_2$")
    plt.gca().set_aspect("equal")

display_contour(H, listeX[1:], listeY[1:], levels = 15) # On reste sur le domaine sans coordonées nulles
plt.show() # TODO: faire des zooms sur les parties intéressantes