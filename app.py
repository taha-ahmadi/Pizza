### Database init for application
import sys
import argparse
### personal modules
from todoModel import TodoModel
import common as c


### run as background
def run():
    pass

# complete
def complete(args):
    TodoModel().complete(args.complete)
### show all todos
def show():
    data = TodoModel().get_all_todos()
    c.display(data)
# Insert new todo
def insert(args):
    TodoModel().insert(args.insert[0], args.insert[1])
    datas = TodoModel().get_all_todos()
    c.display(datas)
# remove todo by ID
def remove(args):
    TodoModel().destroy({"id": args.remove})
    data = TodoModel().get_all_todos()
    c.display(data)
# Truncate table
def truncate():
    TodoModel().truncate()
    show()

def Main():
    parser = argparse.ArgumentParser()
    req = parser.add_argument_group('asdf')
    parser.add_argument("-i", "--insert", help="Insert new todo", type=str, nargs=2)
    parser.add_argument("-r", "--remove", help="Remove todo (id)", type=int)
    parser.add_argument("-s", "--show", help="show todos", action='store_true')
    parser.add_argument("-c", "--complete", help="Cancel operation")
    parser.add_argument("--cancel", help="Cancel operation", action='store_true')
    parser.add_argument("--truncate", help="Truncate table", action='store_true')
    parser.add_argument("--display", help="Display todos", action='store_true')
    args = parser.parse_args()

    if args.insert:
        print(args)
        insert(args)
    if args.remove:
        remove(args)
    if args.show:
        show()
    if args.complete:
        complete(args)
    if args.truncate:
        truncate()

if __name__ == "__main__":
    Main()