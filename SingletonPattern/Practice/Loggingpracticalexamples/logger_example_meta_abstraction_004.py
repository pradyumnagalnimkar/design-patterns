from abc import abstractmethod
import logging
import threading


# Define a metaclass singleton that inherits from ABCMeta
class SingletonMeta(type):
    # Initialise a dictionary to store instances of singleton class
    _instances = {}
    # Initialise a lock to ensure thread-safe singleton implementation
    _lock = threading.Lock()

    # Override the __call__ method to control how the class is instantiated
    def __call__(cls, *args, **kwargs):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # If class is not in instances dictionary then create a new instance
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__()
        return cls._instances[cls]

class BaseLogger(metaclass=SingletonMeta):
    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def critical(self, message):
        pass


class MyLogger(BaseLogger):
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("execution_logs.log")
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("\n%(asctime)s - [%(filename)s - %(lineno)s] - [%(levelname)s] - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message):
        self._logger.debug(message, stacklevel=2)

    def info(self, message):
        self._logger.info(message, stacklevel=2)

    def warning(self, message):
        self._logger.warning(message, stacklevel=2)

    def error(self, message):
        self._logger.error(message, stacklevel=2)

    def critical(self, message):
        self._logger.critical(message, stacklevel=2)
