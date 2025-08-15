class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message = 'unknow exception has found'):
        self.message = message
        super().__init__(self.message)

class InvalidInput(ValueError):
    def __init__(self, message = 'invalid input'):
        self.message = message
        super().__init__(self.message)
        
