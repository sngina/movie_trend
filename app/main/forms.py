from flask_wtf import FlaskForm # this will help us create a form.
from wtforms import   StringField , TextAreaField ,SubmitField # creation of textfields
from wtforms.validators  import Required # this one ensures that all the fields are filled


class ReviewForm(FlaskForm):
  title = StringField('Review title', validators=[Required()]) # 2 para 1st = label 2nd = list of validtors
  review = TextAreaField('Movie review')
  submit = SubmitField('Submit')

 #updating our bio to say something interesting about us...
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')