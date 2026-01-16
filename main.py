from flask import Flask
from faker import Faker
from flask_cors import CORS
CORS(app)
fake = Faker()

app = Flask(__name__)

data = []
for _ in range (20):
fake.name()
@app.route("/")
def hello_world():
    s = request.args.get("name")
    out = {

    }
    return "<p>Hello, World!</p>"
    @app.post("/pippo")
    def crea_qualcosa():
        data = request.get_json()
        print(data)
        return {}. 204 
app.run("0.0.0.0",11000,debug=True)