import numpy as np
import matplotlib.pyplot as plt

# Définir la fonction f(x) = x
def f(x):
    return x

# Générer des valeurs de x
x = np.linspace(-10, 10, 100)

# Calculer les valeurs de f(x) pour chaque x
y = f(x)

# Créer le graphique
plt.plot(x, y)

# Afficher le graphique
plt.show()