import logging
from colorama import init, Fore, Style

# 初始化colorama
init()

# 创建Logger对象
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 定义一个输出到终端并使用颜色的Handler
class ColorHandler(logging.StreamHandler):
    def emit(self, record):
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
handler = ColorHandler()
logger.addHandler(handler)

# 输出不同级别的日志
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
