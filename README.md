# RPG-Personagem — Flask MVC

Front-end para geração de atributos (**Clássico**, **Heróico** e **Aventureiro**), escolha de **Raça** e **Classe**.
Usa Flask com arquitetura MVC (model/controllers/templates + service).

## Rodando localmente

```bash
python -m venv .venv
# Ative o ambiente:
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python app.py  # http://127.0.0.1:5000
```

## Arquitetura (MVC)

- **model/**: entidades (`entities.py`) e estratégias de atributos (`attributes.py`).
- **services/**: orquestra a geração (`generation_service.py`).
- **controllers/**: rotas Flask (`character_controller.py`).
- **templates/**: views Jinja (`base.html`, `index.html`, `character.html`).
- **static/**: CSS/JS simples.
- **app.py**: cria app e registra blueprint.

## Requisitos atendidos

- **3 modos de distribuição**: Clássico (3d6), Heróico (4d6 drop lowest), Aventureiro (2d6 + 6).
- **Raça e Classe**: 3 raças (Humano, Elfo, Anão) e 3 classes (Guerreiro, Mago, Ladino) com listas de habilidades.
- **Reaproveita classes**: `model/` separado.
- **Arquitetura MVC**.
- **Usa Flask**.

## Roteiro rápido para vídeo (2–4 min)

1. Objetivo & tecnologias.
2. Pastas (MVC) e responsabilidades.
3. `model/attributes.py` (estratégias Clássico/Heróico/Aventureiro).
4. `model/entities.py` (raças, classes, bônus raciais).
5. Fluxo: controller → service → model → template.
6. Demonstração: gerar personagem e usar Rerrolar.
