from flask import Flask
from controllers.character_controller import bp as character_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-key"  # ajuste para produção
    app.register_blueprint(character_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
