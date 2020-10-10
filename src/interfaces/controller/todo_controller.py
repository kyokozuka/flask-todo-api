from src.domain.todo_domain import Todo
from src.usecases.todo_interactor import TodoInteractor
from src.interfaces.database.todo_repository import TodoRepository

class TodoController:
    def __init__(self, db_session):
        self.todo_repo = TodoRepository(db_session)
        self.todo_interactor = TodoInteractor(self.todo_repo)
    
    def view(self):
        todos = self.todo_interactor.todos()
        return todos
    
    def create(self, data):
        todo_name = data['todo']
        content = data['content']
        user = data['user']
        self.todo_interactor.add(todo_name=todo_name, content=content, user=user)
        
    def update(self, data):
        id = int(data['id'])
        todo_name = data['todo']
        content = data['content']
        user = data['user']
        self.todo_interactor.update(id, todo_name, content, user)
    
    def is_done(self, data):
        id = int(data['id'])
        is_done = data['is_done']
        self.todo_interactor.is_done(id, is_done)
        
    def remove(self, data):
        id = int(data['id'])
        self.todo_interactor.delete(id=id)