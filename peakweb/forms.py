from flask_wtf import FlaskForm
from wtforms.fields import TextField, IntegerField
from wtforms.validators import Required


class TestSuiteForm(FlaskForm):
    """Represents a new test suite form

    This class represents a new test suite form. It uses flask-wtf form fields
    and validators to construct the form and validate input.

    """
    description = TextField(u'Description')
    url = TextField(u'Test URL')
    nodes = IntegerField(u'Nodes', validators=[Required()])
    requests_node = IntegerField(u'Requests / node', validators=[Required()])
