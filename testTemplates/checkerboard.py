from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def check1():
    return render_template("checkerboard.html", x = 7, y = 7)


@app.route('/<x>/<y>')
def check2(x, y):
    return render_template("checkerboard.html", x = int(x), y = int(y))


if __name__=="__main__":
    app.run(debug=True)

