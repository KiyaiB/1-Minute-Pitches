from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

# from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Share your comment:',validators=[DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    category = SelectField('Type',choices=[('interview','Inspirational pitch'),('product','love pitch'),('promotion','Educational pitch')],validators=[DataRequired()])
    submit = SubmitField('Submit')