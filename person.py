class Person:
    def __init__(self, name):
        self.name = name
        self.id = None
        
    def __str__(self):
        return self.name
    
    def set_id(self, id):
        raise NotImplementedError('set_id not implemented')

    def get_id(self):
        return self.id