from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class FileForm(FlaskForm):
    file = FileField('C Source Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
