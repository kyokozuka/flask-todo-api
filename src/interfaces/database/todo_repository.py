from src.domain.todo_domain import Todo
from src.usecases.todo_repository import abstractTodoRepository


class TodoRepository(abstractTodoRepository):
    def __init__(self, db_session):
        self.db_session = db_session
    
    def find_all(self):
        data =Todo.query.all()
        return data
    
    def create_todo(self, todo: Todo):
        self.db_session.add(todo)
        self.db_session.commit()
        
    def update_todo(self, id: int, todo: Todo):
        _todo = self.db_session.query(Todo).filter(Todo.id==id).first()
        _todo.todo_name = todo.todo_name
        _todo.content = todo.content
        _todo.user = todo.user
        self.db_session.commit()
        
    def is_done(self, id: int, is_done: bool):
        _todo = self.db_session.query(Todo).filter(Todo.id==id).first()
        _todo.is_done = is_done
        self.db_session.commit()
        
    def delete_todo(self, id: int):
        todo = self.db_session.query(Todo).filter(Todo.id==id)
        self.db_session.delete(todo)
        self.db_session.commit()
