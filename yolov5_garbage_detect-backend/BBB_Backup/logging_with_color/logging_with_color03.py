import logging
from colorama import init, Fore, Style


def get_logger(level=logging.INFO):
    # 初始化colorama
    init(autoreset=True)

    # 创建Logger对象
    logger = logging.getLogger()
    logger.setLevel(level)

    # 定义一个输出到终端并使用颜色的Handler
    class ColorHandler(logging.StreamHandler):
        def __init__(self, stream=None, level=logging.NOTSET):
            super().__init__(stream=stream)
            self.level = level

        def emit(self, record):
            if record.levelno >= self.level:
                if record.levelno >= logging.ERROR:
                    color = Fore.RED  # 红色
                elif record.levelno >= logging.WARNING:
                    color = Fore.YELLOW  # 黄色
                elif record.levelno >= logging.INFO:
                    color = Fore.GREEN  # 绿色
                else:
                    color = Style.RESET_ALL  # 默认颜色
                message = self.format(record)
                message = color + message + Style.RESET_ALL  # 恢复默认颜色
                stream = self.stream
                stream.write(message)
                stream.write(self.terminator)

    # 创建ColorHandler对象，并添加到Logger中
    handler = ColorHandler(level=level)
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    logger = get_logger(logging.DEBUG)
    # 输出不同级别的日志
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
