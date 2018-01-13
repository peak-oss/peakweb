
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required


class TestSuiteForm(FlaskForm):
    description = TextField(u'Description')
    url = TextField(u'Test URL')
    nodes = IntegerField(u'Nodes', validators=[Required()])
    requests_node = IntegerField(u'Requests / node', validators=[Required()])
