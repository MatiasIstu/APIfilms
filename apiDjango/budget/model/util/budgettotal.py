import re


def budget_total(films):

    total = 0
    for film in films:  
        total = total + format_budget(film['budget'])
    
    return total
        
def format_budget(budget:str):
    
    aux = re.findall("\d+", budget)
    if not aux:
        aux.append('0')

    return int(aux[0] or 0)
