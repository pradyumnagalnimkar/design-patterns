import logging
import threading

"""
    1. Define a metaclass singleton that inherits from type
    2. Initialise a dictionary to store instances of singleton class
    3. Initialise a lock to ensure thread safe singleton implementation
    4. Override the __call__ method to control how class is instantiated
    5. Acquire the lock to ensure thread safety
    5. If the class is not in dictionary then create a new instance using super(SingletonMeta, cls).__call__
"""


# Define a metaclass Singleton that inherits from the type
class SingletonMeta(type):
    # Initialise a dictionary to store instances of singleton class
    _instances = {}
    # Initialise a lock to ensure thread safe singleton implementation
    _lock = threading.Lock()

    # Override the __call__ method to control how class is instantiated
    def __call__(cls,name, *args, **kwargs):
        # Acquire lock to ensure thread safety
        with cls._lock:
            # If the class is not in dictionary then create a new instance
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(name)
            return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self, name):
        self._initialise_logger(name)

    def _initialise_logger(self, name):
        # Set up logger
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)

        # Create file handler and set its level to DEBUG
        file_handler = logging.FileHandler("execution_logs.log", 'w')
        file_handler.setLevel(logging.DEBUG)

        # Create console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter and add it to handlers
        formatter = logging.Formatter("%(asctime)s-%(filename)s-%(levelname)s-%(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def get_logger(self):
        return self._logger
