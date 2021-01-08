# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class Cable:
    """This class is used for cable instances to connect houses and batteries"""

    def __init__(self, cable_id, size, connection):
        self.cable_id = cable_id
        self.size = size
        self.connection = {}

    def add_connection(self, battery, house):
        self.connection[battery] = house

