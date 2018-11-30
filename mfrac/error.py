#error.py
#Script By jiho2007

class FractionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
