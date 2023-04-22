import sqlite3
import date

def add_task(conn, c, name, duedate):
    # generate the created date
    created_date = date.today()

    # add a task record
    c.execute("INSERT INTO tasks (createdate, duedate, task) VALUES (?,?,?)",
        (created_date, duedate, name))

    # commit the record
    conn.commit()

    # print a message to the user
    print("Task added:", name)


def delete_task(conn, c, record_id):

    # try to delete a record
    try:
        c.execute("DELETE FROM tasks WHERE id = ?", record_id)
    except sqlite3.Error as error:
        #message to user on failure
        print("Failed to delete record from sqlite table", error)

    # commit the record
    conn.commit()


def record_exists(conn, c, record_id):
    c.execute("SELECT * FROM tasks WHERE id = ?", record_id)
    record = c.fetchone()

    if record:
        return True
    else:
        return False


def print_tasks(c):
        # c.execute("SELECT id, createdate, duedate,task FROM tasks")
        c.execute("SELECT * FROM tasks")
        tasks = c.fetchall()

        if len(tasks) == 0:
            print("No tasks in database")
        else:
            for task in tasks:
                print("ID:", task[0],
                      "Created:", task[1],
                      "Due date:", task[2],
                      "Task:", task[3])
