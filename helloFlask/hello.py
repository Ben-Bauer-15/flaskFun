from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')          
def hello_world():
    return render_template('index.html', name = "Ben")

@app.route('/dojo')
def response():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    if name == 'john':
        return "Hi John!"
    else:
        return "Hi " + name

@app.route('/repeat/<repeats>/<input>')
def repeat(repeats, input):
    repeats = int(repeats)
    return input * repeats


@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing



                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
