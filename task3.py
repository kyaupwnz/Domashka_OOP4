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
class TodoList:
    def __init__(self):
        self.tasks = []

    def __repr__(self):
        return str(self.tasks)

    def __setitem__(self, key, value):
        self.tasks.insert(key, value)


    def __getitem__(self, value):
        return self.tasks[value]

    def __delitem__(self, key):
        del self.tasks[key]

todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
print(todo_list)
#[Сдать домашку (создано 2022-12-08 12:34:33), Выпить кофе (создано 2022-12-08 12:34:33)]

print(todo_list[0])
#Сдать домашку (создано 2022-12-08 12:34:33)

del todo_list[0]
print(todo_list)
#[Выпить кофе (создано 2022-12-08 12:34:33)]
