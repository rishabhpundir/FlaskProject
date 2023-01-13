from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b2085744424de9102e6c34b0c53d6484'

# to generate a random SECRET_KEY for (csrf)
# in console
# 1. python
# 2. import os
# 3. print(os.urandom(16).hex())

@app.route('/')
def home():
    pizzas = ['pepperoni', 'mushroom', 'chicken tikka', 'margarita', 45]
    text = "This Is <strong>Bold</strong> TEXT."
    return render_template('home.html', text=text, pizzas=pizzas)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
        
        
class NameForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
# Flash messages for the event, category is mentioned because it can be used to determine color of the alert
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash(message="Form submitted successfully!", category="success")
    return render_template('name.html', form=form, name=name)
        

if __name__ == "__main__":
    app.run(debug=True)