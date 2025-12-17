Organisation des exercices

Convention proposée:

- Dossier par semaine: WeekNN (ex: Week01)
- Sous-dossier par jour: DayN (ex: Day1)
- Nom de fichier: Type_Title.py (ex: exo_add_numbers.py, daily_fizzbuzz.py)

Exemples:

- Week01/Day1/exo_add_numbers.py
- Week02/Day3/daily_challenge_reverse.py

Utilisation:

1. Utiliser le script tools/create_exercise.py pour créer une nouvelle structure automatiquement:

   python tools/create_exercise.py --week 1 --day 2 --type exo --title "add_numbers"

2. Le script crée le dossier (si nécessaire) et écrit un fichier template.

Si vous voulez que je réorganise vos fichiers existants, dites-moi comment vous voulez les mapper (semaine/jour/type).
