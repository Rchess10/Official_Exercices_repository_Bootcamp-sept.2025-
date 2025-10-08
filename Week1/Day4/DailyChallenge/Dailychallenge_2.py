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
        start_index = self.current_idx * self.page_size
        end_index = start_index + self.page_size
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
        if isinstance(page_num, int):
            pn = page_num
        elif isinstance(page_num, str) and page_num.isdigit():
            pn = int(page_num)
        else:
            raise ValueError("Page number must be an integer.")

        if 1 <= pn <= self.total_pages:
            self.current_idx = pn - 1
        else:
            raise ValueError(f"Invalid page number. Page must be between 1 and {self.total_pages}.")

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        if self.total_pages > 0:
            self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(map(str, visible_items))

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("Page 1 (initiale):", p.get_visible_items())

print("--- Test next_page et enchaînement ---")
p.next_page().next_page()
print("Page 3:", p.get_visible_items())

print("--- Test last_page ---")
p.last_page()
print("Dernière Page:", p.get_visible_items())

print("--- Test go_to_page avec une page valide ---")
p.go_to_page(2)
print("Page 2 (via go_to_page):", p.get_visible_items())

print("--- Test previous_page et first_page enchaînés ---")
p.previous_page().first_page()
print("Première Page (après navigation):", p.get_visible_items())

print("\n--- Test de la méthode __str__ sur la page 1 ---")
print(str(p))

print("\n--- Test des erreurs (ValueError) ---")
try:
    p.go_to_page(10)
except ValueError as e:
    print("Test d'erreur (hors de portée):", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("Test d'erreur (zéro):", e)

try:
    p_err = Pagination(alphabetList, "non_nombre")
except ValueError as e:
    print("Test d'erreur (page_size non entier):", e)

try:
    p_err_neg = Pagination(alphabetList, -5)
except ValueError as e:
    print("Test d'erreur (page_size négative):", e)