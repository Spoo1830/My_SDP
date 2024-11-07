from flask import Flask

app2 = Flask(__name__)

@app2.route("/")
def home():
    return "<h1>welcome to DevOps</h1>"

if __name__ == "__main__":
    app2.run(host="0.0.0.0", port=5000)