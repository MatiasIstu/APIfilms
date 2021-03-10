from .util.csv_reader import parse_films
from .util.budgettotal import budget_total
from .util.avgbudget import budget_promedio


def costo_pais(pais):
    films = parse_films()
    return budget_total(films[pais.upper()])

def costo_promedio_pais(pais):
    films = parse_films()
    return budget_promedio(films[pais.upper()])

