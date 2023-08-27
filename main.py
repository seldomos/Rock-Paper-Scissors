# Rock-Paper-Scissors Game
# seldomos (Alex Kuvaldin)
# *forked from 0xPoma/Rock-Paper-Scissors

import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from assets import menu, check

dictionary_game = {1: "Rock",
                   2: "Paper",
                   3: "Scissors"}

exit_log = ["invalid literal for int() with base 10: 'q'",
            "invalid literal for int() with base 10: 'Q'",
            "invalid literal for int() with base 10: 's'",
            "invalid literal for int() with base 10: 'S'"]

X = ['Сравнение кол-ва побед']
user_win_list = [0]
computer_win_list = [0]
X_axis = np.arange(len(X))


def main():
    while True:
        menu()
        target = randint(1, 3)

        try:
            user_in = int(input())
            if user_in > 3 or user_in < 1:
                print("Введите допустимое значение!")
                time.sleep(2)
                continue
        except ValueError as err:
            if str(err) == exit_log[0] or str(err) == exit_log[1]:
                sys.exit()
            elif str(err) == exit_log[2] or str(err) == exit_log[3]:
                plt.bar(X_axis-0.25, user_win_list, 0.4,
                        label='Победы пользователя')
                plt.bar(X_axis+0.25, computer_win_list,
                        0.4, label='Победы компьютера')
                plt.xticks(X_axis, X)
                plt.ylabel("Количество побед")
                plt.title("Итоговая статистика")
                plt.legend()
                plt.show()
                time.sleep(2)
                continue
            else:
                print("Неверный ввод, введите число")
                time.sleep(2)
                continue
        else:
            if check(user_in, target) == 0:
                print(dictionary_game[user_in], "vs",
                      dictionary_game[target], "- Ничья!")
                time.sleep(2)
                continue
            elif check(user_in, target) == 1:
                print(dictionary_game[user_in], "vs",
                      dictionary_game[target], "- Победа!")
                user_win_list[0] += 1
                time.sleep(2)
                continue
            elif check(user_in, target) == 2:
                print(dictionary_game[user_in], "vs",
                      dictionary_game[target], "- Поражение!")
                computer_win_list[0] += 1
                time.sleep(2)
                continue


if __name__ == "__main__":
    main()
