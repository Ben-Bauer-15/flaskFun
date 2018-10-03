from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/danger')
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    # we'll talk about the following two lines after we learn a little more about forms
    return render_template('result.html', form = request.form)
if __name__=="__main__":
    app.run(debug=True) 
