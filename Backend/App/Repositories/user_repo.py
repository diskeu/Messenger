# repo to acces / post user data to the database
from __future__ import annotations
from Backend.App.Models.user import User
from Backend.App.Repositories.base_repo import BaseRepo
from mysql.connector.errors import (
    Error as MysqlBaseError
)

class UserRepo(BaseRepo):
    def __init__(self, logger, cnx):
        super().__init__(logger)
        self.logger = logger
        self.cnx = cnx

    def get_user_info(self, user_id: int, *columns: str) -> User | BaseRepo.RepoError:
        """User - ORM: Given a 'user_id', returns instance of the user class or RepoError"""
        user_model = self.get_info(
            model=User,
            table="messenger.users",
            primary_key=user_id,
            *columns
        )
        return user_model # returns model | RepoError
    

    def post_user(self, *models: User) -> int | BaseRepo.RepoError:
        """
        Given user models, creates a db entry with the specified propertys from the user model
        
        :param model: Instances of the same model class
        :type model: user
        :return: Primary Key[user_id] or RepoError
        :rtype: int | RepoError
        """
        # calling functions to get sql query
        columns, values = self.get_columns_values(*models)
        if not columns or not values: return None # Nothing to insert
        insert_query: str = self.build_insert_query("messenger.users", columns, values)
        
        # flattens the values into one single tuple
        flat_values = tuple(
            x
            for section in values
            for x in section
        )

        # getting cursor
        cursor = self.create_cursor_obj(self.cnx)

        # executing query
        last_id = None
        try:
            cursor.execute(insert_query, flat_values)   # replaces %s with actual values
            last_id = cursor.lastrowid                  # get the inserted id
            
        except MysqlBaseError as err:
            return self.handle_db_error(err)
        
        finally:
            self.cnx.commit()
            cursor.close()
            self.cnx.close()

        return last_id

    def update_single_user(self, user_id, values: dict) -> None | BaseRepo.RepoError:
        """Given a 'user_id', values and a 'mysql.connector.connection_cext.CMySQLConnection', updates the user's values"""
        update_query, insert_values = self.build_update_query(
            table="messenger.users",
            update_val=values,
            other_statement="WHERE user_id = %s"
        )
        insert_values.append(user_id)

        # getting cursor
        cursor = self.create_cursor_obj(self.cnx)
        try:
            cursor.execute(update_query, insert_values)   # replaces %s with actual values
            
        except MysqlBaseError as err:
            return self.handle_db_error(err)
        
        finally:
            self.cnx.commit()
            cursor.close()
            self.cnx.close()

    def delete_users(self, users: tuple[int]) -> None| BaseRepo.RepoError:
        """Given a list of user_ids, deletes the users"""
        # making condition
        user_statement = ["%s" for _ in range(len(users))]
        condition = f"WHERE user_id IN ({", ".join(user_statement)})"

        # getting delete query
        delete_query = self.build_delete_query(
            "messenger.users",
            condition
        )
        # making sql request
        # getting cursor
        cursor = self.create_cursor_obj(self.cnx)
        try:
            cursor.execute(delete_query, users) # replaces %s with actual values
        except MysqlBaseError as err:
            return self.handle_db_error(err)
        
        finally:
            self.cnx.commit()
            cursor.close()
            self.cnx.close()

from Backend.App.logger_config import setup_logger
from Backend.App.Database.connection import connect
u_r = UserRepo(setup_logger(), connect(config_file_location="/Users/TimJelenz/Desktop/messenger/Backend/Configurations/mysql.conf", user="root"))
u_r.get_info(User, "messenger.users", ("user_id", 1000))
