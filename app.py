from flask import Flask
from web.routes import configure_routes

app = Flask(__name__, template_folder="web/templates")
app.secret_key = "my_key"
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
