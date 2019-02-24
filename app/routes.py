import os

from flask import render_template, jsonify, request
from werkzeug.utils import secure_filename

from app import app
from app.forms import FileForm
from runner import Runner


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()

    if form.validate_on_submit():
        file = request.files['file']

        filename = secure_filename(file.filename)

        full_filename = '/tmp/shotgun/' + filename

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        r = Runner(full_filename)
        r.run()

        return jsonify(r.run_results)

    context = {
        'title': 'Home',
        'form': form,
    }

    return render_template('index.html', **context)


@app.route('/success', )
def success():
    return 'success'
