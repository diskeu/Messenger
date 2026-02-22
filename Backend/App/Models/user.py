# User Model for users_table
from datetime import datetime, date
from Backend.App.Models.base_model import BaseModel

class User(BaseModel):
    def __init__(self,
        user_id: int,
        user_name: str,
        hashed_password: str,
        email: str,
        created_at: datetime,
        birth_date: date,
        last_seen: datetime | None = None
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.hashed_password = hashed_password
        self.email = email
        self.created_at = created_at
        self.last_seen = last_seen
        self.birth_date = birth_date
    
    def __repr__(self):
        return "<Name {}> <Id {}>".format(self.user_name, self.user_id)
