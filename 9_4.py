from random import choice

#  Lambda-функция:
print('Lambda-функция:\n')

first = 'Мама мыла раму'
second = 'Рамена мало было'

r = list(map(lambda x, y: x == y, first, second))
print(r)

#  Замыкание:
print('Замыкание: в файле')


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for i in data_set:
            if isinstance(i, str):
                file.write(i + '\n')
            elif isinstance(i, list):
                for j in i:
                    file.write(str(j) + ' ')
                print('\n')
            else:
                raise TypeError(f"Невозможно записать данные типа {type(i)}")
        file.close()

    return write_everything


write = get_advanced_writer('example_2.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#  Метод __call__:
print('Метод __call__:\n')


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
