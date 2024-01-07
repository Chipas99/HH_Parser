from src.config import config
from src.utils import create_database, save_data_to_database
from src.DBManager import DBManager


def main():
    employers_ids = [
        1740,  # Яндекс
        78638,  # Тинькофф
        3529,  # Сбер
        39305,  # Газпром
        41825,  # Первый канал
        80,  # АльфаБанк
        1122462,  # Skypro
        907345,  # Лукойл
        4934,  # Билайн
        239363  # Роснефть-НТЦ
    ]

    print('В базе представлена информация по открытым вакансиям компаний Яндекс, Тинькофф, Сбер, Газпром,\n'
          'Первый канал, Альфабанк, Билайн, Лукойл, Skypro, Роснефть-НТЦ с сайта HeadHunter.ru\n')

    params = config()
    databasename = 'cw'
    create_database(databasename, params)
    save_data_to_database(employers_ids, databasename, params)
    dbmanager = DBManager(params)

    while True:

        extra = input(
            'Введите 1, чтобы получить список всех компаний с количеством вакансий по каждой из них\n'
            'Введите 2, чтобы получить список всех компаний с их вакансиями, зарплатой и ссылкой на вакансию\n'
            'Введите 3, чтобы получить среднюю зарплату по всем вакансиям из базы\n'
            'Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
            'Введите 5, чтобы получить список вакансий по ключевому слову из их названия\n'
            'Введите слово "Стоп", чтобы завершить работу\n'
        )

        if extra.lower() in ('стоп', 'stop'):
            print('Спасибо, что воспользовались нашей программой.\n'
                  ' До свидания!')
            break
        elif extra == '1':
            print(f'{dbmanager.get_companies_and_vacancies_count()}\n')

        elif extra == '2':
            print(f'{dbmanager.get_all_vacancies()}\n')

        elif extra == '3':
            print(f'{dbmanager.get_avg_salary()}\n')

        elif extra == '4':
            print(f'{dbmanager.get_vacancies_with_higher_salary()}\n')

        elif extra == '5':
            keyword = input('Введите слово для поиска вакансий: \n')
            print(f'{dbmanager.get_vacancies_with_keyword(keyword)}\n')

        else:
            print('Неверный ввод. Повторите')


if __name__ == '__main__':
    main()
