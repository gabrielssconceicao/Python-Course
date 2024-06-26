from collections import namedtuple
from typing import NamedTuple

Carta = namedtuple(
    "Carta",
    ["valor", "naipe"],
    defaults=["VALOR", 'NAIPE']
)


class Card(NamedTuple):
    valor: str = "VALOR"
    naipe: str = "NAIPE"


as_espadas = Card("A", "Espadas")
carta2 = Carta()
print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)
print(carta2)
print(carta2._asdict())
