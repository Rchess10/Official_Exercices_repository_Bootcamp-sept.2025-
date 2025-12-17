#!/usr/bin/env python3
"""Helper script to create exercise folders and a template file.

Usage:
    python tools/create_exercise.py --week 1 --day 2 --type exo --title add_numbers
"""
import argparse
import os
from pathlib import Path


TEMPLATE = '''"""
Exercice: {title}
Week: {week}
Day: {day}
Type: {type}
"""

def make_exercise(week:int, day:int, exo_type:str, title:str, base_path:Path):
    week_name = f"Week{week:02d}"
    day_name = f"Day{day}"
    dest_dir = base_path / week_name / day_name
    dest_dir.mkdir(parents=True, exist_ok=True)
    safe_title = title.strip().replace(' ', '_')
    filename = f"{exo_type}_{safe_title}.py"
    file_path = dest_dir / filename
    if file_path.exists():
        print(f"Le fichier existe déjà: {file_path}")
        return file_path
    content = TEMPLATE.format(title=title, week=week, day=day, type=exo_type)
    content += '\n\nif __name__ == "__main__":\n    pass\n'
    file_path.write_text(content, encoding='utf-8')
    print(f"Créé: {file_path}")
    return file_path


def main():
    parser = argparse.ArgumentParser(description='Créer un exercice (dossier + fichier template)')
    parser.add_argument('--week', type=int, required=True, help='Numéro de la semaine (ex: 1)')
    parser.add_argument('--day', type=int, required=True, help='Numéro du jour (ex: 1)')
    parser.add_argument('--type', required=True, help='Type: exo | daily | challenge')
    parser.add_argument('--title', required=True, help='Titre court pour le fichier (ex: add_numbers)')
    parser.add_argument('--base', default='.', help='Chemin de base du workspace')
    args = parser.parse_args()
    base_path = Path(args.base).resolve()
    make_exercise(args.week, args.day, args.type, args.title, base_path)


if __name__ == '__main__':
    main()
