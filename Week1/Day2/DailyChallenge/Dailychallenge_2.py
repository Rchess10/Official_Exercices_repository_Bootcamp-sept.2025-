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
print(type(decoded))
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

# matrix = [
#     ['7', 'i', 'i'],
#     ['T', 's', 'x'],
#     ['h', '%', '?'],
#     ['i', ' ', '#'],
#     ['s', 'M', ' '],
#     ['$', 'a', ' '],
#     ['#', 't', '%'],
#     ['^', 'r', '!']
# ]

# rows = matrix_str.split('\n')
