from othello.planche import Planche
from othello.joueur import JoueurHumain
from othello.exceptions import ErreurExceptionCoup


class Partie:
    def __init__(self):
        self.planche = Planche()

        self.couleur_joueur_courant = "noir"

        self.tour_precedent_passe = False

        self.deux_tours_passes = False

        self.coups_possibles = []

        self.initialiser_joueurs()

    def initialiser_joueurs(self):
        self.joueur_noir = self.creer_joueur('noir')
        self.joueur_blanc = self.creer_joueur('blanc')
        self.joueur_courant = self.joueur_noir

    def creer_joueur(self, couleur):
        if couleur.lower() == "blanc":
            return JoueurHumain("blanc")
        else:
            return JoueurHumain("noir")

    def obtenir_couleur_joueur_adverse(self):
        if self.couleur_joueur_courant == "noir":
            return "blanc"
        return "noir"

    def valider_position_coup(self, position_coup):
        # On lance une exception pour tout type de situation qui empêche un joueur
        # de jouer un coup.
        valide = True
        erreur = ""

        if not self.planche.position_valide(position_coup):
            erreur = "Position coup invalide: la position entrée est à l'extérieur de la planche de jeu.\n"
            raise ErreurExceptionCoup(erreur)
        elif self.planche.get_piece(position_coup) is not None:
            erreur = "Position coup invalide: une pièce se trouve déjà à cette position.\n"
            raise ErreurExceptionCoup(erreur)
        elif position_coup not in self.coups_possibles:
            erreur = "Position coup invalide: cette pièce ne peut pas faire de prise.\n"
            raise ErreurExceptionCoup(erreur)
        return valide, erreur

    def tour(self, position):
        # On joue le tour présent en vérifiant s'il termine la partie.
        # Sinon, on valide le coup et on procède au changement de couleur si tout est dans l'ordre.
        # On vérifie finalement si un coup peut être joué dans le tour suivant.
        self.coups_possibles = self.planche.lister_coups_possibles_de_couleur(self.couleur_joueur_courant)

        if not self.valider_position_coup(position)[0]:
            return
        self.planche.jouer_coup(position, self.couleur_joueur_courant)
        if self.partie_terminee():
            return

        self.changer_couleur()
        self.verifier_prochain_tour()

    def verifier_prochain_tour(self):
        # On vérifie si un coup peut être joué dans ce tour, si oui on retourne,
        # sinon on passe le tour.
        self.coups_possibles = self.planche.lister_coups_possibles_de_couleur(self.couleur_joueur_courant)

        if len(self.coups_possibles) == 0:
            self.passer_tour()
            return
        else:
            self.tour_precedent_passe = False

    def passer_tour(self):
        # On passe le tour et on met l'attribut de vérification du tour_precedent à vrai.
        # L'exception est lancée et affiche l'erreur au joueur avec une description.
        self.tour_precedent_passe = True
        self.changer_couleur()
        self.coups_possibles = self.planche.lister_coups_possibles_de_couleur(self.couleur_joueur_courant)

        if len(self.coups_possibles) == 0:
            self.deux_tours_passes = True
            return
        joueur_adverse = self.obtenir_couleur_joueur_adverse()
        raise ErreurExceptionCoup("Le joueur " + joueur_adverse + " ne peut pas jouer avec l'état actuel de la planche,"
                                                           " il doit donc passer son tour.\n")

    def changer_couleur(self):
        if self.joueur_courant.couleur == "noir":
            self.joueur_courant = self.joueur_blanc
            self.couleur_joueur_courant = "blanc"
        else:
            self.joueur_courant = self.joueur_noir
            self.couleur_joueur_courant = "noir"

    def partie_terminee(self):
        # S'il y a 64 pièces sur la planche ou que deux tours sont passés, la partie est terminée.
        if len(self.planche.cases.keys()) > 63 or self.deux_tours_passes is True:
            return True
        return False

    def determiner_gagnant(self):
        # Maintenant que la partie est terminée, on compte les pièces sur la planche pour déclarer le résultat.
        noir = 0
        blanc = 0
        deux_tours = ""

        if self.deux_tours_passes:
            deux_tours = "Deux tours passés, fin de partie.\n"

        for coords in self.planche.cases:
            if self.planche.cases[coords].couleur == "noir":
                noir += 1
            else:
                blanc += 1

        if noir > blanc:
            return(deux_tours + "Le gagnant est le joueur noir avec " + str(noir) + " pièces.")
        elif noir < blanc:
            return(deux_tours + "Le gagnant est le joueur blanc avec " + str(blanc) + " pièces.")
        else:
            return(deux_tours + "Match nul.")
