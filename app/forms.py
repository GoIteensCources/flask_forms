import flask_wtf
from wtforms import StringField, SubmitField, EmailField, PasswordField, IntegerField, BooleanField, validators
from wtforms.validators import ValidationError


def my_validate_password(form, field):
    if len(field.data) < 4:
        raise ValidationError('NAME must be less than 10 and more then 4 characters')


def my_validate_password_1(form, field):
    if "1" in field.data:
        raise ValidationError('NAME 1 characters')


class SubcriptionForm(flask_wtf.FlaskForm):
    name = StringField("Ім'я")
    email = StringField("Email")
    submit = SubmitField("Відправити")


class RegistrationForm(flask_wtf.FlaskForm):
    name = StringField("Ім'я", validators=[
        validators.InputRequired(),
        my_validate_password,
        my_validate_password_1
    ])
    email = EmailField("Email",
                       validators=[
                           validators.InputRequired()
                       ])

    password = PasswordField("Password", [
                            # validators.Length(min=4, max=10),
                            validators.InputRequired(),
                            my_validate_password
    ])
    age = IntegerField("Вік", validators=[validators.Optional()])
    remember = BooleanField("Запам'ятати мене")
    submit = SubmitField("Відправити")
