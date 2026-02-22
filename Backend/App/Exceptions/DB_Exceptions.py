class ExistingAttributeError(Exception):
    """Raised when a value in the db already exists"""
    def __init__(self, message):
        super().__init__(message)

class QuerySyntaxError(Exception):
    """Raised when the syntax of the sql query has an error"""
    def __init__(self, message):
        super().__init__(message)

class ModelError(Exception):
    """Raised when a non-valid Model gets parsed in a function parameter"""
    def __init__(self, message):
        super().__init__(message)

class SqlReturnTypeError(Exception):
    """Raised when something is wrong with the sql-return-type"""
    def __init__(self, message):
        super().__init__(message)