class DeckEmptyError(Exception):
    def __init__(self, message, errors):            
        super().__init__("empty deck error")
        self.errors = errors