import numpy as np
from card import Card
from pouch import Pouch


class Table:
    """
    Игровой стол, используется для создания игроков и запуска игры.
    """

    def __init__(self, users: int) -> None:
        self._users: int = users
        self._cards: list = []
        self.add_users()

    def add_users(self) -> None:
        """
        Используется для создания карточек игроков при инициализации класса Table
        """
        count_npc: int = 0
        for index in range(self._users):
            user = input('Введите имя игрока, если поле пустое - игрок компьютер: ')
            if user:
                card = Card(user=user, npc=False)
            else:
                count_npc += 1
                card = Card(user=f'Компьютер №{count_npc}', npc=True)
            self._cards.append(card)

    def print_all_cards(self) -> None:
        [card.print_card() for card in self._cards if card]

    def __str__(self) -> str:
        return ', '.join([card.user for card in self._cards])

    def game(self) -> None:
        """
        Запуск игры Loto.
        """
        pouch: Pouch = Pouch()
        step_of_game: int = 0
        for barrel in pouch:
            if self._users <= 1:
                for card in self._cards:
                    if card:
                        print(f'Выиграл {card.user}')
                        print('Конец игры.')
                        return
                print('Никто не выиграл.')
                return
            step_of_game += 1
            print(f'Новый бочонок: {barrel}, ход № {step_of_game}.')
            for index, card in enumerate(self._cards):
                if not card:
                    continue
                card.print_card()
                check_card = card.check_number_in_card(barrel)
                if not card._npc:
                    while True:
                        answer = input(f'{card.user}, есть ли цифра {barrel} на вашей карточке? (Y/n)')
                        if answer in ['Y', 'y', 'Д', 'д', 'Yes', 'yes', 'Да', 'да']:
                            if check_card:
                                print('Цифра есть на карточке - она зачеркивается и игра продолжается.')
                                break
                            else:
                                print(f'Цифры на карточке нет - игрок {card.user} проигрывает.')
                                self._cards[index] = ''
                                self._users -= 1
                                break
                        elif answer in ['N', 'n', 'Н', 'н', 'No', 'no', 'Нет', 'нет']:
                            if check_card:
                                print(f'Цифра на карточке есть - игрок {card.user} проигрывает.')
                                self._cards[index] = ''
                                self._users -= 1
                                break
                            else:
                                print('Цифры на карточке нет - игра продолжается.')
                                break
                        else:
                            print('Вы ввели ерунду, попробуйте еще раз.')
                            continue
                    if card.check_card_to_end():
                        print(f'Выиграл {card.user}!')
                        return
                if card.check_card_to_end():
                    print(f'Выиграл {card.user}!')
                    return
