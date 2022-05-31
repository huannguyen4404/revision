import sys


def open_file(name, mode):
    try:
        file = open(name, mode)
    except IOError as e:
        print(str(e))
        sys.exit(1)
    return file


def remove_task(task_id):
    file = open_file("tasks.txt", "r")
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    del tasks[int(task_id)]


def list_task():
    file = open_file("tasks.txt", "r")
    tasks = file.readlines()
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        print("|-{0}----{1}----{2}----|".format("index", "title", "content"))
        tasks = [task.strip() for task in tasks]
        for i in range(len(tasks)):
            title, content = tasks[i].split('|')
            print("|-{0}--{1}----{2}-|".format(i, title, content))
    file.close()


def add_task(title, content):
    task = title + "|" + content
    file = open_file("tasks.txt", "a")
    file.write(task + "\n")
    file.close()


if __name__ == "__main__":
    print("this is some print statement")
