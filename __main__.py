"""
Module principal du package othello.
"""

from interface.interface_othello import Fenetre

if __name__ == '__main__':
    # Création d'une instance de Partie.
    f = Fenetre()
    f.mainloop()