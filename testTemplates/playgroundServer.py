from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play1():
    return render_template("playground.html", boxes = 3, color = 'blue')

@app.route('/play/<x>')
def play2(x):
    return render_template("playground.html", boxes = int(x), color = 'blue')

@app.route('/play/<x>/<color>')
def play3(x, color):
    return render_template("playground.html", boxes = int(x), color = color)

if __name__=="__main__":
    app.run(debug=True)

