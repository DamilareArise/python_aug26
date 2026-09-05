class TodoBackend:
    __name = None
    __database = []
    
    def __init__(self, name):
        self.__name = name
    
    def create_todo(self, todo):
        if not todo:
            return "Todo can't be empty"
        self.__database.append(todo)
        return "Todo added successfully"
    
    def get_todos(self):
        return self.__database
    
    def get_name(self):
        return self.__name
    

class Hello:
    pass