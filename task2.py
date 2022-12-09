import datetime
class Task:
    def __init__(self, content):
        self.__content = content
        self.__date = datetime.datetime.now()

    def __keys(self):
        return self.__content, self.__date

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__content == other.__content
        return NotImplemented

    def __hash__(self):
        return hash(self.__content)

    def __repr__(self):
        return f'{self.__content} (создано {self.__date.strftime("%Y-%d-%m %H:%M:%S")})'

    def __str__(self):
        return f'{self.__content} (создано {self.__date.strftime("%Y-%d-%m %H:%M:%S")})'

    def __len__(self):
        return len(self.__content)

    def __bool__(self):
        return bool(len(self.__content))



todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks) 
print(len([item for item in todo_list if not item]))
#2

