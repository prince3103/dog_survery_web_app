from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, SelectField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('Please enter Breed of your Dog?', validators = [DataRequired()])
    mood = RadioField("Mood of your Dog:", choices=[("Happy","Happy"), ("Excited","Excited")],
        default='Happy')
    food_choice = SelectField(u"Please choose Dog Food", choices=[("Biscuit","Biscuit"),
        ("Milk","Milk"), ("Beef", "Beef"), ("Chiken","Chiken")])
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        flash(f"Breed: {session['breed']}, Mood: {session['mood']}, Food Choice: {session['food_choice']}")
        return redirect(url_for("index"))


    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
