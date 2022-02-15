# from GoalChef.models import User
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, SelectField
import email_validator
from wtforms.fields.html5 import DateField
# lists

# gender
gender_lst = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

# Height
height_ft_list = [(1, '1ft'), (2, '2ft'), (3, '3ft'), (4, '4ft'), (5, '5ft'), (6, '6ft'), (7, '7ft')]

height_in_list = [(0, '0in'), (1, '1in'), (2, '2in'), (3, '3in'), (4, '4in'), (5, '5in'), (6, '6in'), (7, '7in'), (8, '8in'),
                  (9, '9in'), (10, '10in'), (11, '11in')]

# Activity level
activity_level_list = [(1, 'Sedentary (little to no activity each week) '), (2, 'Lightly Active (1-2 days per week) '),
                       (3, 'Moderately Active (3-5 days per week) '), (4, 'Very Active (4-7 days per week) '), ]

# Weight loss target
# Height
weight_target = [(1, '1lb'), (2, '2lb'), (3, '3lb'), (4, '4lb'), (5, '5lb')]


class RegistrationForm(Form):
    first_name = StringField("", [validators.Length(min=3, max=50),
                                  validators.regexp("^[a-zA-Z0-9'-]*$",message="Alphanumeric characters, ', or - only"),
                                  validators.DataRequired(message="Please fill out this field.")])
    last_name = StringField("", [validators.Length(min=3, max=50),
                                 validators.regexp("^[a-zA-Z0-9'-]*$", message="Alphanumeric characters, ', or - only"),
                                 validators.DataRequired(message="Please fill out this field.")])
    email_address = StringField("", [validators.Length(min=3, max=50),
                                     validators.Email(),
                                     validators.DataRequired(message="Please fill out this field.")])
    birth_date = DateField("", format='%Y-%m-%d')
    # birth_date = StringField("")
    phone_number = StringField("", [validators.DataRequired(message="Please fill out this field.")])
    password = PasswordField("",[validators.Length(min=8, max=24)
                                ,validators.DataRequired(message="Please fill out this field."),
                                  validators.EqualTo(fieldname="confirm", message="Passwords must match")])
    confirm = PasswordField("", [validators.DataRequired(message="Please fill out this field.")])

    # def validate_first_name(self):


class CreateGoal(Form):
    gender = SelectField(label="", choices=gender_lst, description="Gender")

    height_ft = SelectField(label="", choices=height_ft_list, description="height-ft")

    height_in = SelectField(label="", choices=height_in_list, description="height-in")

    starting_weight = IntegerField("", [validators.DataRequired(message="Please fill out this field.")])

    goal_weight = IntegerField("", [validators.DataRequired(message="Please fill out this field.")])

    activity_level = SelectField(label="", choices=activity_level_list, description="activity-level")


    weekly_target = SelectField(label="", choices=weight_target)


class LoginForm(Form):
    email_address = StringField("", [validators.Length(min=3, max=50),
                                     validators.DataRequired(message="Please fill out this field.")])
    password = PasswordField("", [validators.DataRequired(message="Please fill out this field.")])
