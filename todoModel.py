# Get todos
from database import Database

class TodoModel:

    __db = None
    
    def __init__(self):
        TodoModel.__db = Database.getInstance()

    def get_all_todos(self):
        return TodoModel.__db.query("SELECT * FROM todos")

    def insert(self,do, deadline):
        return TodoModel.__db.insert('todos',{
            "do": do,
            "deadline": deadline
        })

    def destroy(self,data):
        return TodoModel.__db.delete('todos', data)

    def complete(self, id):
        TodoModel.__db.update('todos',{
            "is_complete": 1
        }, "WHERE id="+id)
    def truncate(self):
        return TodoModel.__db.truncate("todos")