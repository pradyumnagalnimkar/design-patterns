# from logging_classic_singleton import SingletonLogger
# from logger_example_meta_003 import Logger
from logger_example_meta_abstraction_004 import MyLogger
# 1st way
# logger = SingletonLogger.get_instance().logger

# 2nd way
# logger = Logger(__name__).get_logger()

# 3rd way & more efficient way
logger = MyLogger()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

logger2 = MyLogger()
logger.error("This is an error message")
logger.critical("This is a critical message")

print(logger2 is logger)

logger3 = MyLogger()
print(logger3 is logger2)
logger.warning("This is a warning message")
