import numpy as np


class Card:
    ''' Карточка лото. 15 случайных цифр, по 5 цифр в каждом ряду,
    цифры ранжировны по столбцам, по десяткам на каждый столбец,
    как на сайте  "Спортлото".
    '''

    def __init__(self, user: str = '', npc: bool = True):
        self._card = self.make_random_array()
        self.user = user
        self._npc = npc

    def make_random_array(self) -> np.array:
        # получение 15 случайных цифр (с учетом того, чтоб в каждый столбец помещались цифры одного десятка)
        border = [1, 10, 20, 30, 40, 50, 60, 70, 80, 91]
        rand = []
        for i in range(len(border) - 1):
            arr = np.arange(border[i], border[i + 1])
            np.random.shuffle(arr)
            rand.extend(list(arr[:2]))

        for ind in range(3):
            index = np.random.randint(0, len(rand))
            del rand[index]

        # # 1 создание матрицы по 5 чисел в строке, каждый десяток в своем столбце
        arr_number = [[], [], []]
        index1 = np.random.choice([0, 1, 2])
        for item in rand:
            index1 = index1 % 3
            arr_number[index1].append(item)
            index1 += 1

        arr_card = np.full((3, 9), 0)

        for index1 in range(len(arr_number)):
            for item in range(len(arr_number[index1])):
                index2 = arr_number[index1][item] // 10
                if index2 == 9:
                    index2 = 8
                # print('index1 -', index1, ' index2-', index2, ' item-', item)
                arr_card[index1][index2] = arr_number[index1][item]

        # Замена типа элементов на srt,
        card = arr_card.astype(np.str_)
        # Замена нулей пробелами
        card[card == '0'] = ' '
        return card

    def print_card(self) -> None:
        print('-' * 8, f'Игрок {self.user}.', '-' * 9)
        for row in range(len(self._card)):
            for item in range(len(self._card[row])):
                print(f'| {self._card[row][item]:>2}', end='')
            print('|')
        print('-' * 37)

    def check_number_in_card(self, number: str) -> bool:
        for row in range(len(self._card)):
            for item in range(len(self._card[row])):
                if self._card[row][item] == number:
                    self._card[row][item] = '✖'
                    return True
        return False

    def check_card_to_end(self) -> bool:
        for row in range(len(self._card)):
            for item in range(len(self._card[row])):
                if self._card[row][item] != ' ' and self._card[row][item] != '✖':
                    return False
        return True

    def __str__(self) -> str:
        return self.user
