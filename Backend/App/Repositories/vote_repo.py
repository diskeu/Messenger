# Repo to access / post data, related to the votes-table
from __future__ import annotations
from Backend.App.Models.vote import Vote
from Backend.App.Repositories.base_repo import BaseRepo

class VoteRepo(BaseRepo):
    def __init__(self, logger, cnx):
        super().__init__(logger)
        self.logger = logger
        self.cnx = cnx

    # def get_users_vote(self, post_id: int, user_id: int, *columns: str) -> int | BaseRepo.RepoError:
    #     """Given a post_id, user_id and """

    #     # SELECT post_id, community_id, post_creator, SUM(v.vote), image_url
    #     # FROM messenger.posts p
    #     # INNER JOIN messenger.votes v
    #     #     ON p.post_id = v.post_id
    #     # LEFT OUTER JOIN messenger.images i
    #     #     USING (post_id)
    #     # WHERE p.post_id IN ()
    #     # ;
    #     def get_posts_summary(self, *post_id: int) -> list[dict[any]] | BaseRepo.RepoError:
    #     self.get_all("messenger.posts p", "INNER JOIN messenger.votes v ON p.post_id = v.post_id LEFT OUTER JOIN messenger.images i USING (post_id) WHERE p.post_id IN({post_ids_placeholders}))".format(', '.join("%s" for _ in post_ids)), post_ids, "post_id", "community_id", "post_creator", "SUM(v.vote)", "image_url")
    #     post_model = self.get_info(
    #         Post,
    #         "messenger.posts",
    #         {"post_id": post_id},
    #         *columns
    #     )
    #     return post_model # model | RepoError
    
    def get_users_vote(self, user_id, *post_ids: str) -> dict[int, int] | BaseRepo.RepoError:
        """
        Given a user and posts, returns the status of the users vote in format dict \n
        -> {post_id: -1 | 1} for all values where user has placed a vote or RepoError
        """

        # -- Selecting all votes from the user on specific posts
        # SELECT post_id, vote
        # FROM messenger.votes v
        # WHERE user_id = 1002 AND post_id IN (1, 2, 3, 4)
        # ;

        condition = "WHERE user_id = %s AND post_id IN ({})".format(
                ", ".join(
                    "%s" for _ in range(len(post_ids))
                )
            )
        sql_return_val: list = self.get_all(
            "messenger.votes",
            condition,
            (user_id, *post_ids),
            "post_id, vote"
        )
        if isinstance(sql_return_val, self.RepoError): return sql_return_val

        # formatting into {post_id: -1 | 1, ...}
        post_id_to_vote = {post_vote.get("post_id"): post_vote.get("vote") for post_vote in sql_return_val}
        return post_id_to_vote

    def insert_post(self, *models: Post) -> None | BaseRepo.RepoError:
        """Given post models, inserts them into the DB, returns None | RepoError"""
        return self.post_model(     # None | RepoError
            "messenger.posts",
            *models
        )

    def update_single_post(self, post_id, values: dict) -> None | BaseRepo.RepoError:
        """Given a 'post_id', values and a 'mysql.connector.connection_cext.CMySQLConnection', updates the post's values"""
        update_query, insert_values = self.build_update_query(
            table="messenger.posts",
            update_val=values,
            other_statement="WHERE post_id = %s"
        )
        insert_values.append(post_id)

        # executing statement
        return self.execute_write(update_query, *insert_values) # None | RepoError

    def delete_posts(self, *posts: int) -> None| BaseRepo.RepoError:
        """Given a list of post_ids, deletes the corresponding posts"""
        # making condition
        post_statement = ["%s" for _ in range(len(posts))]
        condition = f"WHERE post_id IN ({", ".join(post_statement)})"

        # getting delete query
        delete_query = self.build_delete_query(
            table="messenger.posts",
            condition=condition
        )
        # executing statement
        return self.execute_write(delete_query, *posts)
    
from Backend.App.logger_config import setup_logger
from Backend.App.Database.connection import connect
from Backend.App.Models.vote import Vote

c_r = VoteRepo(setup_logger(), connect("/Users/TimJelenz/Desktop/messenger/Backend/Configurations/mysql.conf", "root"))
c_r.get_users_vote(1002, 1, 2, 3, 32, 12, 44)