from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, EmailField, SubmitField
from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b2085744424de9102e6c34b0c53d6484'

# Add a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Initialise the DB
db = SQLAlchemy(app)

# Create a DB Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Kolkata')))
    
    #Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')
def home():
    pizzas = ['pepperoni', 'mushroom', 'chicken tikka', 'margarita', 45]
    text = "This Is <strong>Bold</strong> TEXT."
    return render_template('home.html', text=text, pizzas=pizzas)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
        

class UserForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    email = EmailField("Enter Your Email", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
@app.route('/user', methods=['GET', 'POST'])
def enter_user_data():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user_data = User(
                name=form.name.data,
                email=form.email.data
            )
            db.session.add(user_data)
            db.session.commit()
            flash(message=f"User '{name}' added successfully!", category="success")
        else:
            flash(message="User with this email already exists! Please try again.", category="warning")
    # users = User.query.order_by(User.date_added)        
    return render_template('user.html', form=form)
        

if __name__ == "__main__":
    app.run(debug=True)