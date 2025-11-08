from flask import Flask, render_template
from init import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", aps=len(df_aps), cli=len(df_clients))


if __name__ == "__main__":
    app.run(debug=True)
