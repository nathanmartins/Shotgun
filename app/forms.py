from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired

from app.models import Result


class FileForm(FlaskForm):
    file = FileField('C Source Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        res = Result.query.filter_by(filename=self.file.data.filename).first()
        if res is not None:
            self.file.errors.append('File with that name already exists')
            return False

        return True
