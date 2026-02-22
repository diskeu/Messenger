# Image Model for images table
from Backend.App.Models.base_model import BaseModel

class Image(BaseModel):
    def __init__(
        self,
        image_id: int,
        image_path: str,
        post_id: int
    ):
        self.image_id = image_id
        self.image_path = image_path
        self.post_id = post_id
    
    def __repr__(self):
        return "<Image Id {}> <Post Id {}".format(self.image_id, self.post_id)
                