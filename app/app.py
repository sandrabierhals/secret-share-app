from flask import Flask
from routes import main
from database import init_db

app = Flask(__name__)
app.register_blueprint(main)
init_db()

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True,
    use_reloader=False
)