from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
#adds fillable forms and clickable button 
class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = StringField('quantity', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

