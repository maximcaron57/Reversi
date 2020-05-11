class Piece:
    """
    Classe modélisant une pièce d'un jeu d'Othello.
    """
    def __init__(self, couleur):
        """
        La méthode spéciale __init__ d'une classe est appelée lorsqu'on instancie un nouvel objet. Elle peut prendre
        des paramètres supplémentaires (ici, "couleur"), qui sont les paramètres nécessaires lorsqu'on crée un nouvel
        objet. Le mot clé "self" permet de stocker des informations dans l'instance de l'objet. Chaque instance a son
        propre espace mémoire et peut donc contenir des valeurs différentes dans ses variables membres.

        Args:
            couleur: couleur de la pièce ("blanc", "noir"), un string.
        """
        assert couleur in ["blanc", "noir"], "Piece: couleur invalide."

        self.couleur = couleur

    def est_blanc(self):
        """
        Retourne si la pièce est de couleur blanche.

        Returns:
            True si la pièce est de couleur blanche, False autrement.
        """
        return self.couleur == "blanc"

    def est_noir(self):
        """
        Retourne si la pièce est de couleur noire.

        Returns:
            True si la pièce est de couleur noire, False autrement.
        """
        return self.couleur == "noir"

    def echange_couleur(self):
        """
        Fait le changement de couleur de la pièce lorsqu'elle est mangée.
        """
        self.couleur = "noir" if self.est_blanc() else "blanc"

    def __repr__(self):
        """
        Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Piece pour l'affichage.
        Faire un print(une_piece) affichera un caractère unicode représentant le dessin d'une pièce.
        """
        if self.est_noir():
            return "\u26C2"
        else:
            return "\u26C0"
