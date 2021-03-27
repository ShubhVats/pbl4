from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/myapp")
def index():
    return render_template("FinalCode.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
