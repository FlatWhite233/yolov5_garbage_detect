import logging
import sys

# 定义一个输出到终端并使用颜色的Handler
class ColorHandler(logging.StreamHandler):
    def emit(self, record):
        if record.levelno >= logging.ERROR:
            color = '\033[31m'  # 红色
        elif record.levelno >= logging.WARNING:
            color = '\033[33m'  # 黄色
        elif record.levelno >= logging.INFO:
            color = '\033[32m'  # 绿色
        else:
            color = '\033[0m'  # 默认颜色
        message = self.format(record)
        message = color + message + '\033[0m'  # 恢复默认颜色
        stream = self.stream
        stream.write(message)
        stream.write(self.terminator)

# 创建Logger对象，并添加ColorHandler
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = ColorHandler(sys.stdout)
logger.addHandler(handler)

# 输出不同级别的日志
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
