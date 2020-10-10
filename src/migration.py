import sys
sys.dont_write_bytecode = True

import domain.todo_domain
from infrastructure.sqlite3_handler import Base, engine

class Migration:
    
    def init_db(self):
        Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    m = Migration()
    m.init_db()