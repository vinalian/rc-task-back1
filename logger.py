# logger file

from loguru import logger
from os import path


def setup_logger():
    workdir = path.dirname(path.abspath(__file__))

    logger.add(f'{workdir}/log/log.log',
               level="DEBUG",
               format="[{level}] {time} {function} {message}",
               rotation="1 week",
               compression="zip")
