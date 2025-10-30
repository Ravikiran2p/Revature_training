class AgeNotEnoughError(Exception):
    def __init__(self, message='You are a minor'):
        super().__init__(message)
