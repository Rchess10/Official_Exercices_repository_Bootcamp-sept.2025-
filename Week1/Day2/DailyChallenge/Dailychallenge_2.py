# The matrix string, each line is a row in the grid
matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Split the string into rows
rows = matrix_str.split('\n')
print(type(rows[0])) 
print(type(rows))    

# Build the matrix as a list of lists (2D list)
matrix = [list(row) for row in rows]

matrix = []
for row in rows:
    ligne = list(row)      # On transforme la chaîne en liste de caractères
    matrix.append(ligne)   # On ajoute cette liste à la matrice

print(matrix)

                # Find the number of columns (all rows are the same length)
num_cols = len(matrix[0])
num_rows = len(matrix)
print(num_cols)
print(num_rows)

message = ""
for col in range(num_cols):
    for row in range(num_rows):
        char = matrix[row][col]
        message += char
print(message)

decoded = ""
previous_is_alpha = False

for char in message:
    if char.isalpha():
        if not previous_is_alpha and decoded and decoded[-1] != " ":
            decoded += " "  # Ajoute un espace si le caractère précédent n'était pas une lettre
        decoded += char
        previous_is_alpha = True
    else:
        previous_is_alpha = False


print(decoded.strip())

# #char.isalpha() : Vrai si le caractère courant est une lettre, Faux sinon.
# not previous_is_alpha : Vrai si le caractère précédent n’était pas une lettre, Faux si c’était une lettre.
# decoded : Vrai si la chaîne decoded n’est pas vide, Faux si elle est vide.
# decoded[-1] != " " : Vrai si le dernier caractère de decoded n’est pas un espace, Faux si c’est un espace.

# Cycle :

# 1er tour : char = '7' → pas une lettre → previous_is_alpha = False
# 2e tour : char = 'T' → lettre, previous_is_alpha = False, decoded vide → on ajoute 'T', previous_is_alpha = True
# 3e tour : char = 'h' → lettre, previous_is_alpha = True → on ajoute 'h'
# 4e tour : char = 'i' → lettre, previous_is_alpha = True → on ajoute 'i'
# 5e tour : char = 's' → lettre, previous_is_alpha = True → on ajoute 's'
# 6e tour : char = '$' → pas une lettre → previous_is_alpha = False
# 7e tour : char = '#' → pas une lettre → previous_is_alpha = False
# 8e tour : char = '^' → pas une lettre → previous_is_alpha = False
# 9e tour : char = 'i' → lettre, previous_is_alpha = False, decoded = 'This', decoded[-1] != ' ' → on ajoute un espace, puis 'i', previous_is_alpha = True
# 10e tour : char = 's' → lettre, previous_is_alpha = True → on ajoute 's'
# ... etc.
# À chaque fois qu’on passe d’un symbole à une lettre, on ajoute un espace (sauf au début).

