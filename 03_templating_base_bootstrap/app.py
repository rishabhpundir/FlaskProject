from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    pizzas = ['pepperoni', 'mushroom', 'chicken tikka', 'margarita', 45]
    text = "This Is <strong>Bold</strong> TEXT."
    return render_template('home.html', text=text, pizzas=pizzas)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
        
        
# Invalid Server Error url
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
        

if __name__ == "__main__":
    app.run(debug=True)