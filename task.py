import sqlite3
import date
import data
import interface

# create a connection to a database
conn = sqlite3.connect('tasks.db')
# create a cursor object
c = conn.cursor()

# create a table if it does not exist
c.execute(''' CREATE TABLE IF NOT EXISTS tasks 
    ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        createdate TEXT,
        duedate TEXT,
        task TEXT
    )
''')


main_menu_list = ["Add a task",
                "View tasks",
                "Delete a task",
                "Check record existance",
                "Quit"]

# main loop of the program
while True:

    # print menu option
    interface.list(main_menu_list, True, False)

    # get option from user
    choice = input("Enter a option number: ")

    # execute path switch depending on user option
    match choice:
        # add a record
        case "1":

            # get input from the user
            newtask = input("Enter a task: ")

            # get input until valide date
            while True:
                duedate = input("Enter due date(DD-MM-YYYY)")
                if not date.is_valid_date(duedate):
                    print("Incorrect date format, please try again (DD-MM-YYYY)")
                else:
                    break

            data.add_task(conn, c, newtask, duedate)
        
        # view records
        case "2":
            data.print_tasks(c)

        # delete records
        case "3":
            # select all the records from the table
            c.execute("SELECT * FROM tasks")

            # get all the records and put the in a tuple
            tasks = c.fetchall()

            # check the number of records, of none print message
            if len(tasks) == 0:
                print("No tasks.")
            else:
                # print records
                data.print_tasks(c)

                # get the primary key value of the record to delete
                task_num = int(input("Enter Record Id to delete"))

                # check valid id number
                if not data.record_exists(conn, c, (record_id,)):
                    print("Invalid task number.")
                else:
                    # delete the record
                    data.delete_task(conn, c, (task_num,))

        case "4":
            record_id = int(input("Please enter a record number"))
            print(data.record_exists(conn, c, (record_id,)))
        
        # quit
        case "5":
            # break from the match statement
            break

        # unknown input
        case _:
            print("Incorrect menu number")

# close the database
conn.close()