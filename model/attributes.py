import random
from typing import Dict, List

ATTRS = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]

class Dice:
    @staticmethod
    def roll(dice_str: str) -> int:
        # ex.: "3d6" => rola 3 dados de 6 lados
        num, sides = dice_str.lower().split("d")
        total = 0
        for _ in range(int(num)):
            total += random.randint(1, int(sides))
        return total

class Distributor:
    def generate(self) -> Dict[str, int]:
        raise NotImplementedError

class ClassicDistributor(Distributor):
    # Clássico: 3d6 por atributo
    def generate(self) -> Dict[str, int]:
        return {a: Dice.roll("3d6") for a in ATTRS}

class HeroicDistributor(Distributor):
    # Heróico: 4d6 drop lowest
    def generate(self) -> Dict[str, int]:
        values = {}
        for a in ATTRS:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            values[a] = sum(rolls)
        return values

class AdventurerDistributor(Distributor):
    # Aventureiro: 2d6 + 6 por atributo (ajuste se seu livro definir outra fórmula)
    def generate(self) -> Dict[str, int]:
        return {a: (sum(random.randint(1, 6) for _ in range(2)) + 6) for a in ATTRS}

def pick_distributor(mode: str) -> Distributor:
    mode = mode.lower()
    if mode == "classico":
        return ClassicDistributor()
    if mode == "heroico":
        return HeroicDistributor()
    if mode == "aventureiro":
        return AdventurerDistributor()
    raise ValueError("Modo de geração inválido")
