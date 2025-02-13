from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username, email):
        self.id = str(user_id)  # Flask-Login requires an `id` attribute
        self.username = username
        self.email = email
