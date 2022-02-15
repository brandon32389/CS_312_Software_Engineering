from flask import render_template, flash, request, redirect, url_for
from GoalChef.forms import RegistrationForm, LoginForm, CreateGoal
from GoalChef import app, models, db, bcrypt
from datetime import datetime, date
from flask_login import login_user, current_user, logout_user


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # if user is already authenticated, send to appropriate page instead.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm(request.form)
    # print(form.email_address.data, form.password.data)
    # print(form.validate())
    if request.method == 'POST' and form.validate():
        user = models.User.query.filter_by(email_address=form.email_address.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, False)
            flash('You have been logged on successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please try again.', 'danger')
    else:
        return render_template("Login.html", title='Login', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    # if user is already authenticated, send to appropriate page instead.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Creating Registration Form class object
    form = RegistrationForm(request.form)

    # Checking that method is POST and form is valid.
    if request.method == 'POST' and form.validate():

        # Add data from the form to the user object to be inserted.
        user = models.User()
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email_address = form.email_address.data
        #  Format birthdate into datetime data type.
        # user.birth_date = datetime.strptime(form.birth_date.data, '%m/%d/%Y')
        user.birth_date = form.birth_date.data
        user.phone_number = form.phone_number.data
        # Hash the password before sending to the DB.
        user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")

        return render_template("Login.html", form=form)
        # else:
        #     flash("Email already is registered", "warning")
        #     return render_template("Register.html", form=form)

    else:
        # If method is GET, then render form.
        return render_template("Register.html", title='Register', form=form)

# TODO: user can make an many goals as they want. This should be limited so we can display the goal.
@app.route('/goal/', methods=['GET', 'POST'])
def goal():
    foot_conversion = 12
    form = CreateGoal(request.form)

    # Only allow access to this page if the user is authenticated. If not, send them to the login page.
    if current_user.is_authenticated:
        # If post, process the form and insert the record, else send the form to the user.
        if request.method == 'POST' and form.validate():
            goal = models.Goal()
            goal.gender = form.gender.data
            #  Height converted and stored as inches.
            goal.height = (int(form.height_ft.data) * foot_conversion) + int(form.height_in.data)
            goal.starting_weight = form.starting_weight.data
            goal.goal_weight = form.goal_weight.data
            goal.activity_level = form.activity_level.data
            goal.weekly_weight_loss = form.weekly_target.data
            goal.user_id = current_user.id

            db.session.add(goal)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            return render_template("Create_Goal.html", form=form)
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    logout_user()
    flash('You have been logged off successfully.', 'success')
    return redirect(url_for('index'))
