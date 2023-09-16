# Database file

from psycopg2 import connect
from os import environ
from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine


load_dotenv()


host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
db_name = environ.get('DB_NAME')


class Project:
    def __init__(self):
        # psycopg2 connection (SQL)
        with connect(host=host, port=port, user=user, password=password, dbname=db_name) as self.db:
            self.cur = self.db.cursor()

    def create_table(self) -> None:
        """
        Create a new table in the database
        :return: None
        """

        self.cur.execute(
            '''
                create table if not exists public."project"
                    (
                        id SERIAL PRIMARY KEY,
                        project VARCHAR(100),
                        year_2022 FLOAT,
                        year_2023 FLOAT,
                        year_2024 FLOAT,
                        year_2025 FLOAT
                    );
            ''')
        self.db.commit()

    @staticmethod
    def insert_data_with_alchemy(data) -> bool:
        """
        :param data: Pandas object
        :return: true if successful, false otherwise false
        """
        try:
            # sqlalchemy connection (ORM)
            engine = create_engine(
                f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
            )

            data.to_sql(name='project', con=engine, if_exists='append')
            return True
        except Exception as error:
            logger.error(error)
            return False
