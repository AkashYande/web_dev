import sys                
from flask import Flask 
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


app=Flask(__name__)
app.config['SECRET_KEY']='flask_key'

todos=["flask_app","setup env", "build app"]

class TodoForm(FlaskForm):
    todo = StringField('Todo')
    submit = SubmitField("Add To Dos")

@app.route('/', methods=["GET","POST"])
def home():
    if 'todo' in request.form:
        todos.append(request.form['todo'])
    return render_template('index.html', todos=todos, template_form=TodoForm())

if __name__ == '__main__':
    app.run(debug=True)