class MissingParams(Exception):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        params = ', '.join(self.params)
        
        params.strip(', ')

        return f"missing {params}"
    

class AlreadyExists(Exception):
    def __int__(self, entity):
        self.entity = entity

    def __str__(self):
        return f"{self.entity} already exists"
    
class DoesNotExists(Exception):
    def __int__(self, entity):
        self.entity = entity

    def __str__(self):
        return f"{self.entity} does not exists"
    
class InvalidCommandParams(Exception):
    def __init__(self, requiredParams):
        self.requiredParams = requiredParams

    def __str__(self):
        return f"invalid command, required parameters {self.requiredParams}"
    