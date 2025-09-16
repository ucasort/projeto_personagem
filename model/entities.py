from dataclasses import dataclass, field
from typing import List, Dict

# 3 raças (exemplo)
RACES = {
    "humano": {
        "nome": "Humano",
        "bonus": {"CAR": 1},
        "habilidades": ["Adaptável", "Versátil"],
    },
    "elfo": {
        "nome": "Elfo",
        "bonus": {"DES": 1},
        "habilidades": ["Visão no Escuro", "Sentidos Aguçados"],
    },
    "anao": {
        "nome": "Anão",
        "bonus": {"CON": 1},
        "habilidades": ["Resiliência", "Conhecimento de Pedra"],
    },
}

# 3 classes (exemplo)
CLASSES = {
    "guerreiro": {
        "nome": "Guerreiro",
        "habilidades": ["Ataque Extra", "Estilo de Combate"],
        "atributo_chave": "FOR",
    },
    "mago": {
        "nome": "Mago",
        "habilidades": ["Magia Arcana", "Preparar Feitiços"],
        "atributo_chave": "INT",
    },
    "ladino": {
        "nome": "Ladino",
        "habilidades": ["Ataque Furtivo", "Evasão"],
        "atributo_chave": "DES",
    },
}

DEFAULT_ATTRS = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]

@dataclass
class Character:
    nome: str
    raca_id: str
    classe_id: str
    atributos: Dict[str, int] = field(default_factory=dict)
    habilidades: List[str] = field(default_factory=list)

    @property
    def raca(self):
        return RACES[self.raca_id]

    @property
    def classe(self):
        return CLASSES[self.classe_id]

    def aplicar_bonus_raciais(self):
        for k, v in self.raca.get("bonus", {}).items():
            self.atributos[k] = self.atributos.get(k, 0) + v

    def compilar_habilidades(self):
        self.habilidades = list(self.raca.get("habilidades", [])) + list(self.classe.get("habilidades", []))
