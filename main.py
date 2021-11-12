import click
import sys
import os
from item import *


# folders 
__db_location__ = "db"
__item_folder__ = f"{__db_location__}/item"



def init(arguments):

    def db():
        os.makedirs(__item_folder__)



    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()

if __name__ == '__main__':
    arguments = sys.argv[1:]
    

    init(arguments)

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "item":
        if command == "create":
            create_item(*params)
        elif command == "all":
            get_all_items()
        elif command == "view":
            item_view_by_id(*params)
        elif command == "delete":
            item_delete(*params)

