from abc import ABCMeta, abstractmethod

from src.domain.todo_domain import Todo

class abstractTodoRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_all(self):
        pass
    
    @abstractmethod
    def create_todo(self, todo: Todo):
        pass
    
    @abstractmethod
    def update_todo(self, id: int, todo: Todo):
        pass
    
    @abstractmethod
    def is_done(self, id: int, is_done: bool):
        pass
    
    @abstractmethod
    def delete_todo(self, id):
        pass