import numpy as np
from pouch import Pouch
from card import Card
from table import Table
import argparse


def main():
    parser = argparse.ArgumentParser(description='Input players')
    parser.add_argument('-p', '--common_players', help="Input the common number of players.")
    # parser.add_argument('-s', '--save_to_file', nargs='?', help="Save to file .txt.")
    args = parser.parse_args()

    users = 2
    if args.common_players:
        users = int(args.common_players)
    table: Table = Table(users)
    print('-'*41)
    print('Созданы карточки игроков: ', table, '\n', '-'*40)

    table.game()


if __name__ == '__main__':
    main()
