# Community Model for communitys_table
from datetime import datetime
from Backend.App.Models.base_model import BaseModel

class Community(BaseModel):
    def __init__(
        self,
        community_id: int,
        created_at: datetime,
        community_owner: int,
        community_description: str | None = None
    ):
        self.community_id = community_id
        self.community_description = community_description
        self.created_at = created_at
        self.community_owner = community_owner

    def __repr__(self):
        return "<Id {}> <Owner {}>".format(self.community_id, self.community_owner)
        