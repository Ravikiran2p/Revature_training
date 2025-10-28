"""Area  circumference of sq,rect,circle"""

from math import pi
def area_of_square(side):
    """
    :param side: area of square
    :param side: side of a square
    :return: Area of square
    """
    return side*side

def rectangle_area(len,bred):
    """
    :param side: side of a rectangle
    :param side:
    :return:
    """
    return len*bred


def circle_area(red):
    return pi*red**2

def cir_of_circle(red):
    return 2*pi*red