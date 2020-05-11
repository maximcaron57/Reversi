from othello.piece import Piece

from itertools import product

class Planche:

    def __init__(self):
        # Dictionnaire de cases. La clé est une position (ligne, colonne), et la valeur une instance de la classe Piece.
        self.cases = {}

        # Appel de la méthode qui initialise une planche par défaut.
        self.initialiser_planche_par_default()

        # On joue au Othello 8x8
        self.nb_cases = 8

    def get_piece(self, position):
        if position not in self.cases.keys():
            return None

        return self.cases[position]

    def position_valide(self, position):
        return 0 <= position[0] < self.nb_cases and 0 <= position[1] < self.nb_cases

    def obtenir_positions_mangees(self, position, couleur):
        # Pour chaque direction, on vérifie les positions mangees
        positions_mangees = []

        directions = list(product([-1, 0, 1], [-1, 0, 1]))
        directions.remove((0, 0))

        for d in directions:
            positions_mangees += self.obtenir_positions_mangees_direction(couleur, d, position)

        return positions_mangees

    def obtenir_positions_mangees_direction(self, couleur, direction, position):
        couleur_mangee = "blanc" if couleur == "noir" else "noir"

        position_tentee = (position[0] + direction[0], position[1] + direction[1])
        positions_potentiellement_mangees = []

        while True:
            piece = self.get_piece(position_tentee)

            if piece is None:
                break
            else:
                if piece.couleur == couleur_mangee:
                    positions_potentiellement_mangees.append(position_tentee)
                else:
                    return positions_potentiellement_mangees

            position_tentee = (position_tentee[0] + direction[0], position_tentee[1] + direction[1])

        return []

    def coup_est_possible(self, position, couleur):
        # Si au moins une position est mangée, le coup est possible
        return len(self.obtenir_positions_mangees(position, couleur)) > 0 and position not in self.cases.keys()

    def lister_coups_possibles_de_couleur(self, couleur):
        coups_possibles = []

        for position in list(product(range(self.nb_cases), range(self.nb_cases))):
            if position not in self.cases.keys():
                if self.coup_est_possible(position, couleur):
                    coups_possibles.append(position)

        return coups_possibles

    def jouer_coup(self, position, couleur):
        # Si le coup est possible, on effectue les changements à la planche, sinon on retourne une erreur
        if not self.coup_est_possible(position, couleur):
            return "erreur"

        positions_mangees = self.obtenir_positions_mangees(position, couleur)

        self.cases[position] = Piece(couleur)

        for p in positions_mangees:
            self.get_piece(p).echange_couleur()

        return "ok"


    def initialiser_planche_par_default(self):
        self.cases.clear()
        self.cases[(3, 3)] = Piece("blanc")
        self.cases[(3, 4)] = Piece("noir")
        self.cases[(4, 3)] = Piece("noir")
        self.cases[(4, 4)] = Piece("blanc")

    def __repr__(self):
        s = "  +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, self.nb_cases):
            s += str(i)+" | "
            for j in range(0, self.nb_cases):
                if (i, j) in self.cases:
                    s += str(self.cases[(i, j)])+" | "
                else:
                    s += "  | "
            s += str(i)
            if i != self.nb_cases - 1:
                s += "\n  +---+---+---+---+---+---+---+---+\n"

        s += "\n  +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"

        return s