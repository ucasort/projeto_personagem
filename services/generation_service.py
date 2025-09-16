from model.attributes import pick_distributor
from model.entities import Character, DEFAULT_ATTRS

class GenerationService:
    @staticmethod
    def gerar_personagem(nome: str, raca_id: str, classe_id: str, modo: str) -> Character:
        dist = pick_distributor(modo)
        atributos = dist.generate()
        # garante todos os atributos presentes
        for a in DEFAULT_ATTRS:
            atributos.setdefault(a, 10)

        ch = Character(nome=nome.strip() or "Sem Nome", raca_id=raca_id, classe_id=classe_id, atributos=atributos)
        ch.aplicar_bonus_raciais()
        ch.compilar_habilidades()
        return ch
