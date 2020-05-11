from random import choice


class Joueur:
    """
    Classe générale de joueur. Vous est fournie.
    """

    def __init__(self, couleur):
        """
        Le constructeur global de Joueur.

        Args:
            couleur: La couleur qui sera jouée par le joueur.
        """
        assert couleur in ["blanc", "noir"], "Piece: couleur invalide."

        self.couleur = couleur

    def obtenir_type_joueur(self):
        '''
        Cette méthode sera utilisée par les sous-classes JoueurHumain et JoueurOrdinateur.

        Returns:
            Le type de joueur, 'Ordinateur' ou 'Humain'
        '''
        pass

class JoueurHumain(Joueur):
    """
    Classe modélisant un joueur humain.
    """

    def __init__(self, couleur):
        """
        Cette méthode va construire un objet Joueur et l'initialiser avec la bonne couleur.
        """
        super().__init__(couleur)

    def obtenir_type_joueur(self):
        return "Humain"
