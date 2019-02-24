from flask import render_template, redirect

from app import app
from app.forms import FileForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()

    if form.validate_on_submit():
        return redirect('/success')

    context = {
        'title': 'Home',
        'form': form,
    }

    return render_template('index.html', **context)


@app.route('/success',)
def success():
    return 'success'
