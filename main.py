from src.utils import user_hh


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    print('Здравствуйте! Эта программа поможет Вам в поиске вакансий на сайте: HeadHunter \n'
          'Введите цифру 1 или 2: \n'
          '1 - HeadHunter search \n'
          '2 - Закрыть программу. \n')

    while True:
        user_choice_platform = input()
        if user_choice_platform == '1':
            print('HeadHunter')
            user_hh()
            break

        elif user_choice_platform == '2':
            print('До свидания!')
            break
        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    user_interaction()
