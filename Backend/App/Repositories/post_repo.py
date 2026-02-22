# Repo to access / post data, related to the posts-table
from Backend.App.Models.user import post
from Backend.App.Repositories.base_repo import BaseRepo
from mysql.connector.errors import (
    Error as MysqlBaseError
)

class PostRepo(BaseRepo):
    def __init__(self, logger, cnx):
        super().__init__(logger)
        self.logger = logger
        self.cnx = cnx

    def get_post_info(self, post_id: int, *columns: str) -> post | BaseRepo.RepoError:
        """Post - ORM: Given a 'post_id', returns instance of the post class or RepoError """ 
        if type(post_id) != int:
            self.logger.warning(
                "Wrong type of post_id, "
                "prefered type: int, "
                f"given type: {type(post_id)}"
            )
            return self.RepoError(
                False,
                9,
                "Wrong type",
                TypeError(
                "Wrong type of post_id, "
                "prefered type: int, "
                f"given type: {type(post_id)}"
            )
            ) 
        # getting cursor
        cursor = self.create_cursor_obj(self.cnx)
        
        select_query = self.build_select_query("messenger.posts", "post_id = %s", *columns)
        if isinstance(select_query, self.RepoError): return select_query

        try:
            cursor.execute(select_query, (post_id, ))
            post_info: dict = cursor.fetchall()
        except Exception as err:
            return self.handle_db_error(err)

        # defining model with the given sql return
        user_model: user = self.create_model(user_info, user)
        return user_model # returning user_model or RepoError


