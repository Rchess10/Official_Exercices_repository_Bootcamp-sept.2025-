import math

class Pagination():
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = list(items)

        if not isinstance(page_size, int) or page_size <= 0:
            raise ValueError("page_size must be a positive integer.")
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.page_size > 0 else 0

    def get_visible_items(self):
        """Retourne la liste des éléments visibles sur la page actuelle."""
        # Calcule l'index de début pour la tranche de liste (slice).
        # Ex: Si self.current_idx = 0 et self.page_size = 4, start_index = 0 * 4 = 0
        # Ex: Si self.current_idx = 1 et self.page_size = 4, start_index = 1 * 4 = 4
        start_index = self.current_idx * self.page_size
        
        # Calcule l'index de fin pour la tranche de liste. Python gère les dépassements d'index.
        # Ex: Si start_index = 0 et self.page_size = 4, end_index = 0 + 4 = 4
        # Ex: Si start_index = 4 et self.page_size = 4, end_index = 4 + 4 = 8
        end_index = start_index + self.page_size
        
        # Utilise le slicing de liste pour extraire les éléments.
        # self.items[start_index:end_index] renvoie une nouvelle liste contenant les éléments de la plage.
        # Ex: Si self.items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        #    et start_index=0, end_index=4 -> ['a', 'b', 'c', 'd']
        #    et start_index=4, end_index=8 -> ['e', 'f', 'g', 'h']
        return self.items[start_index:end_index]

    def go_to_page(self, page_num):
        """
        Va à un numéro de page spécifique (indexé à partir de 1 pour l'utilisateur).
        Args:
            page_num (int ou numeric-string): Le numéro de page vers lequel naviguer.
                                             Ex: 1, 3, "2"
        Raises:
            ValueError: Si le numéro de page est hors de portée ou n'est pas une valeur entière.
        """
        # Validation et normalisation du numéro de page (page_num).
        if isinstance(page_num, int):
            pn = page_num # Si c'est déjà un entier, on l'utilise.
            # Ex: si page_num = 3, alors pn = 3
        elif isinstance(page_num, str) and page_num.isdigit():
            pn = int(page_num) # Si c'est une chaîne de chiffres, on la convertit en entier.
            # Ex: si page_num = "2", alors pn = 2
        else:
            # Si le type n'est ni int ni une chaîne de chiffres valide, on lève une erreur.
            raise ValueError("Page number must be an integer.")

        # Vérifie si le numéro de page est dans les limites valides (entre 1 et total_pages inclus).
        # Ex: Si self.total_pages = 7, un pn valide serait 1, 2, ..., 7.
        if 1 <= pn <= self.total_pages:
            self.current_idx = pn - 1 # Convertit le numéro de page (1-basé) en index (0-basé) et met à jour.
                                      # Ex: Si pn = 3, self.current_idx = 3 - 1 = 2
        else:
            # Si le numéro de page est invalide, on lève une erreur explicite.
            # Ex: Si pn = 0 ou pn = 10 (et total_pages=7), cela déclenchera l'erreur.
            raise ValueError(f"Invalid page number. Page must be between 1 and {self.total_pages}.")

    def first_page(self):
        """Navigue à la première page."""
        self.current_idx = 0 # Met l'index de la page actuelle à 0.
                             # Ex: si self.current_idx était 3, il devient 0.
        return self # Retourne l'objet lui-même (self) pour permettre l'enchaînement de méthodes.
                    # Ex: p.first_page().get_visible_items()

    def last_page(self):
        """Navigue à la dernière page."""
        if self.total_pages > 0: # S'assure qu'il y a au moins une page (liste non vide).
            self.current_idx = self.total_pages - 1 # Met l'index à la dernière page (total_pages est 1-basé, current_idx est 0-basé).
                                                    # Ex: Si self.total_pages = 7, self.current_idx = 7 - 1 = 6.
        return self # Permet l'enchaînement de méthodes.

    def next_page(self):
        """Avance d'une page."""
        # Vérifie si la page actuelle n'est pas déjà la dernière page.
        # Ex: Si self.current_idx = 6 et self.total_pages = 7, alors 6 < (7 - 1) est Faux (6 < 6).
        # Ex: Si self.current_idx = 2 et self.total_pages = 7, alors 2 < (7 - 1) est Vrai (2 < 6).
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1 # Incrémente l'index de la page actuelle.
                                  # Ex: Si self.current_idx était 2, il devient 3.
        return self # Permet l'enchaînement de méthodes.

    def previous_page(self):
        """Recule d'une page."""
        # Vérifie si la page actuelle n'est pas déjà la première page.
        # Ex: Si self.current_idx = 0, alors 0 > 0 est Faux.
        # Ex: Si self.current_idx = 3, alors 3 > 0 est Vrai.
        if self.current_idx > 0:
            self.current_idx -= 1 # Décrémente l'index de la page actuelle.
                                  # Ex: Si self.current_idx était 3, il devient 2.
        return self # Permet l'enchaînement de méthodes.

    def __str__(self):
        """Retourne une représentation en chaîne de caractères des éléments visibles, un par ligne."""
        visible_items = self.get_visible_items() # Appelle la méthode pour obtenir les éléments de la page actuelle.
                                                 # Ex: visible_items = ['a', 'b', 'c', 'd']
        # map(str, visible_items) convertit chaque élément de la liste en chaîne de caractères.
        # "\n".join(...) joint toutes ces chaînes avec un retour à la ligne entre elles.
        # Ex: "a\nb\nc\nd"
        return "\n".join(map(str, visible_items))

# --- Test Cases ---
alphabetList = list("abcdefghijklmnopqrstuvwxyz") # Crée une liste de lettres de l'alphabet.
                                                  # Ex: ['a', 'b', ..., 'z'] (26 éléments)

# Initialisation de la pagination avec 26 éléments et 4 éléments par page.
# __init__ est appelé :
#   self.items = alphabetList
#   self.page_size = 4
#   self.current_idx = 0
#   self.total_pages = math.ceil(26 / 4) = math.ceil(6.5) = 7
p = Pagination(alphabetList, 4)

print("Page 1 (initiale):", p.get_visible_items())
# get_visible_items est appelé :
#   start_index = 0 * 4 = 0
#   end_index = 0 + 4 = 4
#   Retourne self.items[0:4]
# Output attendu: Page 1 (initiale): ['a', 'b', 'c', 'd']

print("--- Test next_page et enchaînement ---")
# next_page est appelé une première fois : current_idx passe de 0 à 1.
# next_page est appelé une deuxième fois (grâce au return self) : current_idx passe de 1 à 2.
p.next_page().next_page()
print("Page 3:", p.get_visible_items())
# get_visible_items est appelé (current_idx est maintenant 2) :
#   start_index = 2 * 4 = 8
#   end_index = 8 + 4 = 12
#   Retourne self.items[8:12]
# Output attendu: Page 3: ['i', 'j', 'k', 'l']

print("--- Test last_page ---")
# last_page est appelé : current_idx passe à self.total_pages - 1 = 7 - 1 = 6.
p.last_page()
print("Dernière Page:", p.get_visible_items())
# get_visible_items est appelé (current_idx est maintenant 6) :
#   start_index = 6 * 4 = 24
#   end_index = 24 + 4 = 28
#   Retourne self.items[24:28] (Python gère si l'index de fin dépasse la taille de la liste)
# Output attendu: Dernière Page: ['y', 'z'] (les 2 derniers éléments)

print("--- Test go_to_page avec une page valide ---")
# go_to_page(2) est appelé :
#   pn = 2
#   1 <= 2 <= 7 est Vrai.
#   self.current_idx = 2 - 1 = 1.
p.go_to_page(2)
print("Page 2 (via go_to_page):", p.get_visible_items())
# get_visible_items est appelé (current_idx est maintenant 1) :
#   start_index = 1 * 4 = 4
#   end_index = 4 + 4 = 8
#   Retourne self.items[4:8]
# Output attendu: Page 2 (via go_to_page): ['e', 'f', 'g', 'h']

print("--- Test previous_page et first_page enchaînés ---")
# previous_page est appelé : current_idx passe de 1 à 0.
# first_page est appelé (grâce au return self) : current_idx reste à 0.
p.previous_page().first_page()
print("Première Page (après navigation):", p.get_visible_items())
# get_visible_items est appelé (current_idx est maintenant 0) :
#   start_index = 0 * 4 = 0
#   end_index = 0 + 4 = 4
#   Retourne self.items[0:4]
# Output attendu: Première Page (après navigation): ['a', 'b', 'c', 'd']

print("\n--- Test de la méthode __str__ sur la page 1 ---")
# print(str(p)) appelle la méthode __str__ de l'objet p.
# Cette méthode appelle p.get_visible_items() pour obtenir ['a', 'b', 'c', 'd'].
# Puis elle joint ces éléments avec des retours à la ligne.
print(str(p))
# Output attendu:
# a
# b
# c
# d

print("\n--- Test des erreurs (ValueError) ---")
# Test d'une ValueError pour un numéro de page hors de portée.
try:
    p.go_to_page(10) # total_pages = 7, donc 10 est invalide.
except ValueError as e:
    print("Test d'erreur (hors de portée):", e)
    # Output attendu: Test d'erreur (hors de portée): Invalid page number. Page must be between 1 and 7.

# Test d'une ValueError pour un numéro de page égal à 0.
try:
    p.go_to_page(0) # Le premier numéro de page est 1, donc 0 est invalide.
except ValueError as e:
    print("Test d'erreur (zéro):", e)
    # Output attendu: Test d'erreur (zéro): Invalid page number. Page must be between 1 and 7.

# Test d'une ValueError pour une page_size invalide (non entier)
try:
    p_err = Pagination(alphabetList, "non_nombre")
except ValueError as e:
    print("Test d'erreur (page_size non entier):", e)
    # Output attendu: Test d'erreur (page_size non entier): page_size must be a positive integer.

# Test d'une ValueError pour une page_size invalide (négative)
try:
    p_err_neg = Pagination(alphabetList, -5)
except ValueError as e:
    print("Test d'erreur (page_size négative):", e)
    # Output attendu: Test d'erreur (page_size négative): page_size must be a positive integer.