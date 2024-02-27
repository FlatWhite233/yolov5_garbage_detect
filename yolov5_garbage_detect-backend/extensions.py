# extensions.py：解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()

# Windows下Flask报错提示
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 52-55: ordinal not in range(128)
# 解决方案：https://www.cnblogs.com/Flat-White/p/17261697.html

