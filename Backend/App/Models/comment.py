# comment Model for comments table
from Backend.App.Models.base_model import BaseModel

class Comment(BaseModel):
    def __init__(
        self,
        comment_id: int,
        parent_post: int,
    ):
        self.self = self
        self.comment_id = comment_id
        self.parent_post = parent_post
    
    def __repr__(self):
        return "<Comment Id {}> <Parent Post {}>".format(self.comment_id, self.parent_post)