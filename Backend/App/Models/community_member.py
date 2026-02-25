# Community Members Model for community_members table
from datetime import datetime
from Backend.App.Models.base_model import BaseModel

class CommunityMember(BaseModel):
    def __init__(
        self,
        community_id: int,
        user_id: int,
        role: str,
        member_since: datetime,
    ):
        self.community_id = community_id
        self.user_id = user_id
        self.role = role
        self.member_since = member_since

    def __repr__(self):
        return "<Community Id {}> <User Id {}>".format(self.community_id, self.user_id)
    