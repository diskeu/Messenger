# post Model for posts Table
from datetime import datetime
from Backend.App.Models.base_model import BaseModel

class Post(BaseModel):
    def __init__(
        self,
        post_id: int,
        post_creator: str,
        community_id: int | None,
        post_title: str | None,
        post_content: str,
        post_score: int,
        is_sticky: bool,
        created_at: datetime | None # current timestamp
    ):
        self.post_id = post_id
        self.post_creator = post_creator
        self.community_id = community_id
        self.post_title = post_title
        self.post_content = post_content
        self.post_score = post_score
        self.is_sticky = is_sticky
        self.created_at = created_at

    def __repr__(self):
        return "<Post Id {}> <Creator Id {}".format(self.post_id, self.post_creator)