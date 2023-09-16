# run file to start script

from database import database as table
from script.main_script import *
from os import path, environ
from dotenv import load_dotenv
from loguru import logger
from misc.error import *
from logger import setup_logger


load_dotenv()
setup_logger()


def get_file_path():
    workdir = path.dirname(path.abspath(__file__))
    logger.info('Directory: %s' % workdir)

    file = environ.get('FILE_NAME')
    logger.info('File: %s' % workdir)

    file_path = workdir + "/" + file
    logger.info('File_path: %s' % file_path)

    return file_path


def create_database():
    project_table = table.Project()
    project_table.create_table()


def modify_data(data):
    mod_data = data.rename(columns={
        'проект': 'project', '2022': 'year_2022', '2023': 'year_2023',
        '2024': 'year_2024', '2025': 'year_2025'
    })
    return mod_data


def start_script():
    logger.info('Starting script')

    file_path = get_file_path()
    create_database()

    try:
        script = Main_script(file_path)
        script.process_data()
        ready_data = modify_data(script.ready_data)
        table.Project().insert_data_with_alchemy(ready_data)
    except Exception as error:
        logger.error(error)
        raise Script_error(function_name=start_script().__name__,
                           message=error)
    logger.info('Finished script')


if __name__ == '__main__':
    start_script()
