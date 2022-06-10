import sys

ADD, REMOVE, LIST = "add", "remove", "list"


# defines the main function
# the name can be anything you want
def main():
    args = sys.argv
    try:
        command = args[1]
    except IndexError:
        print("Invalid arguments!")
        sys.exit(1)

    if command not in (ADD, REMOVE, LIST):
        print("Invalid command\n Use {0}/{1}/{2}".format(ADD, REMOVE, LIST))
        sys.exit(1)

    if command == ADD:
        title = args[2]
        content = args[3]
        add_task(title, content)
    elif command == REMOVE:
        task_id = args[2]
        remove_task(task_id)
    elif command == LIST:
        list_task()
    else:
        print("invalid command!")


def remove_task(task_id):
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    del tasks[int(task_id)]


def list_task():
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        print("|-{0}----{1}----{2}----|".format("index", "title", "content"))
        tasks = [task.strip() for task in tasks]
        for i in range(len(tasks)):
            title, content = tasks[i].split('|')
            print("|-.formatd--{0}----{1}-|".format(i, title, content))
    file.close()


def add_task(title, content):
    task = title + "|" + content
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()


main()
