"""
    Steps to implement logging mechanism in your project
    1. Set up a logger
    2. Create a file handler and set its level to DEBUG
    3. Create a console handler and set its level to INFO
    4. Create a formatter and add it to handlers
    5. Add handlers to the logger
"""
import logging

# Set up logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level to DEBUG
file_handler = logging.FileHandler("execution_logs.log", mode='w')
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set its level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to handlers
formatter = logging.Formatter("%(asctime)s- %(filename)s- %(levelname)s- %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

###################################################
# Now you can use the logger to output messages
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is an critical message")
