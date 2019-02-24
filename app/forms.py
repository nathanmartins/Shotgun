from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class FileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    file = FileField('C Source Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
