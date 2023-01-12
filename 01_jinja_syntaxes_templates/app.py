from flask import Flask, render_template

app = Flask(__name__)

# jinja text modifiers (can use more than one tag too eg. {{text|safe|lower|trim}})

# safe - let any html tag modification be done
# capitalize - capitalizes first word
# lower - lowers the whole word
# upper - CAPS ALL
# title - first alphabet capital of each word
# trim - all multiple spaces trimmed down to one. Any exttra spaces outside of the sentence are removed
# striptags - strips all markup tags to send plain text


@app.route('/')
def index():
    pizzas = ['pepperoni', 'mushroom', 'chicken tikka', 'margarita', 45]
    text = "This Is <strong>Bold</strong> TEXT."
    return render_template('index.html', text=text, pizzas=pizzas)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)