import logging

def setup_logger(log_dir_path: str = "/Users/TimJelenz/Desktop/messenger/Backend/App/Logs") -> logging.Logger:
    """Function to configure the root logger"""
    # Setting up Logger
    logger = logging.getLogger() # -> returns root logger
    logger.setLevel(logging.DEBUG)

    # Setting up Formatter
    formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # Setting up stream_handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.DEBUG)

    # setting up file_handler
    file_handler = logging.FileHandler(
        filename = "{path}/{filename}".format(path=log_dir_path, filename="base_log.log")
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.WARNING)

    # adding handlers
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    return logger