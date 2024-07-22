import logging
import threading


class SingletonLogger:
    # Initialize a class level variable to None
    _instance = None

    # Initialize a lock to ensure thread-safe Singleton instantiation
    _lock = threading.Lock()

    # Class method to get the SingletonLogger instance
    @classmethod
    def get_instance(cls):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # If an instance of Singleton does not exist , create one
            if cls._instance is None:
                cls._instance = cls()
                # Initialise the logger for singletonLogger instance
                cls._instance._initialise_logger()
            # Return the existing or newly created SingletonLogger instance
            return cls._instance

    def _initialise_logger(self):
        # Set up logger
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler and set its level to DEBUG
        self.file_handler = logging.FileHandler("execution_logs.log", 'w')
        self.file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to handlers
        formatter = logging.Formatter("%(asctime)s-%(filename)s-%(levelname)s-%(message)s")
        self.file_handler.setFormatter(formatter)
        self.console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)