import json
import sys
from os.path import split

nazwapliku = sys.argv[1]
nazwapliku += ".ipynb"
plik = open(nazwapliku, 'r', encoding="utf8")
data = json.load(plik)
code_cells = filter(lambda cell: cell['cell_type'] == 'code' or cell['cell_type'] == 'markdown', data['cells'])

exercise_cells = filter(
    lambda cell: cell['cell_type'] == 'markdown' and cell['source'] and cell['source'][0].startswith("### Ćwiczenie"),
    data['cells'])
exercise_count = len(list(exercise_cells))

def process_cell(cell):
    if cell['cell_type'] == 'code':
        # Zwraca linie kodu bez zmian
        return cell['source']
    elif cell['cell_type'] == 'markdown':
        # Przetwarza każdą linię markdown jako komentarz
        return list(map(lambda line: f"# {line}", cell['source']))


code_lines = map(process_cell, code_cells)
print(f"# Liczba ćwiczeń w notebooku: {exercise_count}")
with open("Zajecia4.py", 'w', encoding='utf-8') as output_file:
    for cell_lines in code_lines:
        print(*cell_lines, sep="", file=output_file)
        print(file=output_file)
