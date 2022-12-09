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
        return str(self.__keys())

    def __str__(self):
        return f'{self.__content} (создано {self.__date.strftime("%Y-%d-%m %H:%M:%S")})'


todo_list = set()
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))
for item in todo_list:
    print(item)

