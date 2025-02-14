from flask_login import UserMixin
from config.dbconnect import DatabaseConnection
db = DatabaseConnection().connection
class User(UserMixin):
    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password  # Store as a hashed password
        self.role = role  # Can be "learner", "industry_professional", or "supervisor"

    def get_id(self):
        return str(self.email)  # Use email as the unique identifier

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "role": self.role,
        }

    @staticmethod
    def from_dict(data):
        return User(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            role=data["role"],
        )
    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, role={self.role})"