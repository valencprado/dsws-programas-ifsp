from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    role = SelectField('Role?:', choices=[])
    submit = SubmitField('Submit')

    def populate_choices(self):
        from hello import Role
        self.role.choices = [(role.id, role.name) for role in Role.query.all()]