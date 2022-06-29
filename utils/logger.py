import sys
from pathlib import Path
from loguru import logger
from loguru._logger import Core as _Core, Logger as _Logger


def get_new_logger():
    logger = _Logger(
        core=_Core(),
        exception=None,
        depth=0,
        record=False,
        lazy=False,
        colors=False,
        raw=False,
        capture=True,
        patcher=None,
        extra={},
    )
    return logger


class Logger():
    LoggingMap = {}
    def __new__(cls, name, level='INFO', is_async=True):
        instance = cls.LoggingMap.get(name)
        if not instance:
            cls.LoggingMap[name] = get_new_logger()
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, level='INFO', is_async=True):
        self.is_async = is_async
        self.logger = self.LoggingMap[name]
        # container = sys.stdout # TODO:
        container = open(Path(__file__).resolve().parent.parent / 'log.log', 'w')
        self.logger.add(
            container,
            format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | '
            '<level>{level: <8}</level> | '
            '<cyan>%s</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>' % name,
            enqueue=is_async,
            level=level
        )

    def debug(self, msg):
        self.logger.debug(msg)
    def info(self, msg):
        self.logger.info(msg)
    def warning(self, msg):
        self.logger.warning(msg)
    def error(self, msg):
        self.logger.error(msg)
