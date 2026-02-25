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
    
    def get_sub_comments(self, post_ids: list, *columns: str) -> list[dict[any]] | BaseRepo.RepoError:
        """Gets all of the comments of specific post_ids"""

        # checking values
        checked_vals = self.check_pk_val({"post_id": post_id for post_id in post_ids})
        if checked_vals != None: return checked_vals # returns RepoError

        select_query: str = "SELECT {selected_columns} FROM messenger.comments WHERE post_id in ({post_ids})".format(
            selected_columns = ", ".join(columns) if columns else "*",
            post_ids = ", ".join("%s" for _ in range(len(post_ids)))
        )
        # returns comments | RepoError
        return self.execute_read(select_query, *post_ids)

    def insert_comment(self, *models: Comment) -> None | BaseRepo.RepoError:
        """Given Comment models, inserts them into the DB, returns None | RepoError"""
        return self.post_model(     # None | RepoError
            "messenger.comments",
            *models
        )

    def update_single_comment(self, comment_id: int, values: dict) -> None | BaseRepo.RepoError:
        """Given a 'comment_id', values and a 'mysql.connector.connection_cext.CMySQLConnection', updates the comment's values"""
        update_query, insert_values = self.build_update_query(
            table="messenger.comments",
            update_val=values,
            other_statement="WHERE comment_id = %s"
        )
        insert_values.append(comment_id)

        # executing statement
        return self.execute_write(update_query, *insert_values) # None | RepoError 
    
    def delete_comments(self, *comment_ids: int) -> None| BaseRepo.RepoError:
        """Given a list of comment_ids, deletes the corresponding comments"""
        # making condition
        statement = ["%s" for _ in range(len(comment_ids))]
        condition = f"WHERE comment_id IN ({", ".join(statement)})"

        # getting delete query
        delete_query = self.build_delete_query(
            table="messenger.comments",
            condition=condition
        )
        # executing statement
        return self.execute_write(delete_query, *comment_ids)
    
from Backend.App.logger_config import setup_logger
from Backend.App.Database.connection import connect

c_r = CommentRepo(setup_logger(), connect("/Users/TimJelenz/Desktop/messenger/Backend/Configurations/mysql.conf", "root"))
print(c_r.get_all("messenger.comments"))