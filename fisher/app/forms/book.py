
from wtforms import Form,StringField, IntegerField
from wtforms.validators import length, number_range

class SearchForm(Form):
    q = StringField(validators=[length(min=1, max=30)])
    page = IntegerField(validators=[number_range(min=1, max=99)], default=1)
