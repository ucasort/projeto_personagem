from flask import Blueprint, render_template, request
from services.generation_service import GenerationService
from model.entities import RACES, CLASSES

bp = Blueprint("character", __name__)

@bp.get("/")
def index():
    return render_template("index.html", races=RACES, classes=CLASSES)

@bp.post("/gerar")
def gerar():
    nome = request.form.get("nome", "")
    raca_id = request.form.get("raca")
    classe_id = request.form.get("classe")
    modo = request.form.get("modo")
    personagem = GenerationService.gerar_personagem(nome, raca_id, classe_id, modo)
    return render_template("character.html", personagem=personagem, modo=modo)

@bp.get("/rerolar")
def rerolar():
    # preserva parâmetros via query string
    nome = request.args.get("nome", "")
    raca_id = request.args.get("raca")
    classe_id = request.args.get("classe")
    modo = request.args.get("modo")
    personagem = GenerationService.gerar_personagem(nome, raca_id, classe_id, modo)
    return render_template("character.html", personagem=personagem, modo=modo)
