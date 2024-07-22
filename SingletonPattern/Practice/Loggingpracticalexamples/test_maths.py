import math
from logger_example_meta_abstraction_004 import MyLogger

def test_add():
    a,b = 10, 20
    logger = MyLogger()
    logger.info(f"Numbers available for addition are {a} & {b}")
    logger.info(f"Addition: {a + b}")

def test_subtract():
    a, b = 10, 20
    logger = MyLogger()
    logger.info(f"Numbers available for subtraction are {a} & {b}")
    logger.info(f"Subtraction: {b - a}")

def test_area_of_circle():
    radius = 2
    logger = MyLogger()
    logger.info(f"Area of circle with radius: {radius} is {math.pi * radius ** 2}")

def test_multiply():
    a, b = 10, 20
    logger = MyLogger()
    logger.info(f"Numbers available for multiply are {a} & {b}")
    logger.info(f"Multiplication: {b * a}")

def test_division():
    a, b = 10, 20
    logger = MyLogger()
    logger.info(f"Numbers available for division are {a} & {b}")
    logger.info(f"Division: {b / a}")
