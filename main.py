import os

from utils.utils import *
from config import config

companies = {
    1776381: "CATAPULTO.RU",
    2324020: "Точка",
    864086: "getmatch",
    2723603: "AERODISK",
    3407499: "IT школа Hello world",
    80660: "Boxberry",
    1008541: "МФТИ",
    2970204: "Отус",
    4759060: "HR Prime",
    5569859: "ARK"
}
DB_NAME = 'vacancies'
params = config()
script_file = os.path.join('scripts', 'queries.sql')

if __name__ == '__main__':
    list_ = get_vacancies(companies)
    create_db(DB_NAME, params)
    print('База данных создана...')
    params.update({'dbname': DB_NAME})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_tables(cur, script_file)
                print(f"Таблицы в БД {DB_NAME} успешно созданы...")

                fill_table_companies(cur, companies)
                print("Таблица companies заполнена...")

                fill_table_vacancies(cur, list_)
                print("Таблица vacancies заполнена...")

                add_foreign_key(cur)
                print("Связывание таблиц успешно...")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    user_interaction(params)