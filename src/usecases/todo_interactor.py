from src.domain.todo_domain import Todo
from src.usecases.todo_repository import abstractTodoRepository

class TodoInteractor:
    def __init__(self, todo_repo: abstractTodoRepository):
        if not isinstance(todo_repo, abstractTodoRepository):
            raise Exception('It is not abstractTodoRepository instance')
        self.todo_repo = todo_repo
    
    def todos(self):
        todos = self.todo_repo.find_all()
        return todos
    
    def add(self, todo_name: str, content: str, user: str):
        t = Todo(todo_name=todo_name, content=content, user=user)
        self.todo_repo.create_todo(todo=t)
    
    def update(self, id: int, todo_name: str, content: str, user: str):
        t = Todo(todo_name=todo_name, content=content, user=user)
        self.todo_repo.update_todo(id=id, todo=t)
    
    def is_done(self, id: int, is_done: bool):
        self.todo_repo.is_done(id=id, is_done=is_done)
        
    def delete(self, id: int):
        self.todo_repo.delete_todo(id)