from GoalChef import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email_address = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    phone_number = db.Column(db.String(20))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    goals = db.relationship('Goal', backref='user', lazy=True)

    #  This is what data is returned for the user class.
    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email_address}', '{self.birth_date}')"


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    starting_weight = db.Column(db.Integer, nullable=False)
    goal_weight = db.Column(db.Integer, nullable=False)
    activity_level = db.Column(db.Integer, nullable=False)
    weekly_weight_loss = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #  This is what data is returned for the user class.
    def __repr__(self):
        return f"User('{self.goal_type_desc}', '{self.starting_weight}', '{self.goal_weight}')"
