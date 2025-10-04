from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ =="__main__":
    app.run(host="192.168.230.11", port="8080",route="/hello")