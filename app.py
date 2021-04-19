from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pageNA")
def pageNA():
    return render_template("pageNA.html")

if __name__ == "__main__":
    app.run(debug=True, port=5010)