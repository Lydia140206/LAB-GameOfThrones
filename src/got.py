import csv
from pathlib import Path
from typing import List, NamedTuple


BatallaGOT = NamedTuple('BatallaGOT',                         
[
('nombre', str),
('rey_atacante', str),
('rey_atacado', str),
('gana_atacante', bool),
('muertes_principales', bool),
('comandantes_atacantes', List[str]),
('comandantes_atacados', list[str]),
('region', str),
('num_atacantes', int|None),
('num_atacados',int|None)
])

def lee_batallas(ruta:str)->List[BatallaGOT]:
    
    """Lee un fichero con las batallas guardadas y devuelve una lista de Batallas."""
    batallas = []
    
    with open(ruta, "r", encoding= "utf-8") as fichero:
        lector = csv.reader(fichero, delimiter=",")
        next(lector)
        for row in lector:
            batalla = BatallaGOT(
                nombre=row[0],
                rey_atacante=row[1],
                rey_atacado=row[2],
                gana_atacante=row[3].lower() == 'true',
                muertes_principales=row[4].lower() == 'true',
                comandantes_atacantes=row[5].split(',') if row[5] else [],
                comandantes_atacados=row[6].split(',') if row[6] else [],
                region=row[7],
                num_atacantes=int(row[8]) if row[8] else None,
                num_atacados=int(row[9]) if row[9] else None
            )
            batallas.append(batalla)
        return batallas 
    
print(lee_batallas('data/battles.csv'))
    
    
def reyes_mayor_menor_ejercito(batallas: List[BatallaGOT]):
    
    """Encuentra los reyes con el mayor y menor ejército y los muestra."""
    
    batalla_mayor = None
    batalla_menor = None

    for batalla in batallas:
        total_ejercito = (batalla.num_atacantes or 0) + (batalla.num_atacados or 0)
        if batalla_mayor is None or total_ejercito > ( (batalla_mayor.num_atacantes or 0) + (batalla_mayor.num_atacados or 0) ):
            batalla_mayor = batalla
        if batalla_menor is None or total_ejercito < ( (batalla_menor.num_atacantes or 0) + (batalla_menor.num_atacados or 0) ):
            batalla_menor = batalla

    print("Rey con mayor ejército:", batalla_mayor.rey_atacante, "Comandantes:", batalla_mayor.comandantes_atacantes)
    print("Rey con menor ejército:", batalla_menor.rey_atacante, "Comandantes:", batalla_menor.comandantes_atacantes)
        
        
if __name__ == "__main__":
    ruta_fichero = Path("data/battles.csv")
    batallas = lee_batallas(ruta_fichero)