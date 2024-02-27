import smtplib
import config
from email.mime.text import MIMEText
from email.header import Header
import random


class EmailOP:
    def __init__(self, host, port, user, password):
        """
        host：邮件服务器地址
        port：邮件服务器端口
        username：邮箱账户名
        password：邮箱账户的授权码（注意是授权码，不是邮箱的登录密码）
        """
        self.user = user
        self.password = password
        self.smtp = smtplib.SMTP()  # 创建SMTP对象
        self.smtp.connect(host=host, port=port)  # 连接到SMTP服务器
        self.smtp.login(user=self.user, password=self.password)  # 登录邮箱

    def send(self, subject, body, recipient_name, recipient_email,
             sender_name='基于深度学习算法的垃圾检测系统'):
        """
        subject：邮件主题
        body：邮件正文
        sender_name：发送者昵称
        recipient_name：收件人昵称
        recipient_email: 收件人邮箱地址
        """
        message = MIMEText(body, 'plain', 'utf-8')
        message['From'] = Header(sender_name)
        message['To'] = Header(recipient_name)
        message['Subject'] = Header(subject)
        self.smtp.sendmail(from_addr=self.user, to_addrs=recipient_email, msg=message.as_string())


# port=25/587
# port=465时连接超时
email_op = EmailOP(host=config.MAIL_SERVER,
                   port=587,
                   user=config.MAIL_USERNAME,
                   password=config.MAIL_PASSWORD)

if __name__ == '__main__':
    captcha = random.randint(10000, 99999)
    email_op.send(recipient_name='1030078310@qq.com',
                  recipient_email='1030078310@qq.com',
                  subject='测试邮件',
                  body=f'您的验证码：{captcha}')

