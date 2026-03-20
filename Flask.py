from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Este é uma API - Flask, Primeira api"
    

if __name__ == "__main__":
    app.run(debug=True)
