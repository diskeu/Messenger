# Repo to acces / post data related to the comments table
from __future__ import annotations
from Backend.App.Models.comment import Comment
from Backend.App.Repositories.base_repo import BaseRepo

class CommentRepo(BaseRepo):
    def __init__(self, logger, cnx):
        super().__init__(logger)
        self.logger = logger
        self.cnx = cnx

    def get_comment_info(self, comment_id: int, *columns: str) -> Comment | BaseRepo.RepoError:
        """Comment - ORM: Getting comment info based on the comment_id, returns Comment | RepoError"""
        comment_model = self.get_info(
            Comment,
            "messenger.comments",
            {"comment_id": comment_id},
            *columns
        )
        return comment_model # model | RepoError
    
    def get_sub_comments(self, post_ids: list, *columns: str) -> dict[tuple] | BaseRepo.RepoError:
        """Gets all of the comments of specific post_ids"""

        # checking values
        checked_vals = self.check_pk_val({"post_id": post_id for post_id in post_ids})
        if checked_vals != None: return checked_vals # returns RepoError

        select_query: str = "SELECT {selected_columns} FROM messenger.comments WHERE post_id in ({post_ids})".format(
            selected_columns = ", ".join(columns) if columns else "*",
            post_ids = ", ".join("%s" for _ in range(len(post_ids)))
        )

        # getting cursor
        cursor = self.create_cursor_obj(self.cnx)
        try:
            cursor.execute(select_query, post_ids)
            comments: dict = cursor.fetchall()
        except Exception as err:
            self.logger.exception(
                f"Something in cursor execution went wrong, returning RepoError"
            )
            return self.handle_db_error(err)
        finally:
            cursor.close()
        return comments

    def insert_comment(self, *models: Comment) -> None | BaseRepo.RepoError:
        """Given Comment models, inserts them into the DB, returns None | RepoError"""
        return self.post_model(     # None | RepoError
            "messenger.comments",
            *models
        )

    def update_single_community(self, community_id, values: dict) -> None | BaseRepo.RepoError:
        """Given a 'community_id', values and a 'mysql.connector.connection_cext.CMySQLConnection', updates the community's values"""
        update_query, insert_values = self.build_update_query(
            table="messenger.communitys",
            update_val=values,
            other_statement="WHERE community_id = %s"
        )
        insert_values.append(community_id)

        # executing statement
        return self.execute_write(update_query, *insert_values) # None | RepoError 
    
    def delete_communitys(self, *community_id: int) -> None| BaseRepo.RepoError:
        """Given a list of community_id, deletes the corresponding community"""
        # making condition
        statement = ["%s" for _ in range(len(community_id))]
        condition = f"WHERE community_id IN ({", ".join(statement)})"

        # getting delete query
        delete_query = self.build_delete_query(
            table="messenger.community",
            condition=condition
        )
        # executing statement
        return self.execute_write(delete_query, *community_id)
        self.get

from Backend.App.logger_config import setup_logger
from Backend.App.Database.connection import connect
from Backend.App.Repositories.post_repo import PostRepo
from Backend.App.Models.post import Post

logger = setup_logger()
cnx = connect("/Users/TimJelenz/Desktop/messenger/Backend/Configurations/mysql.conf", "root")
c_r = CommentRepo(logger, cnx)
clss = Comment(-1, 44)
p_r = PostRepo(logger, cnx)
c_r.insert_comment(clss)
c = c_r.get_sub_comments([44])
print(c)