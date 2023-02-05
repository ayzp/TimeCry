# email相关
from getpass import getpass
import ssl
import smtplib
from email.message import EmailMessage

def TC_sendEmail():
    # EMAIL_ADDRESS = getpass("Email: ")
    EMAIL_ADDRESS = "yu_zhi_peng@126.com"
    EMAIL_PASSWORD = getpass("Password: ")

    # 连接到SMTP服务器，网易的SMTP服务器是：smtp.126.com，端口：25
    smtpObj = smtplib.SMTP("smtp.126.com", 25)

    # 加载证书验证，在登录时进行证书验证 host验证
    context = ssl.create_default_context()

    # 发送邮件信息创建
    subject = 'Python SMTP 邮件测试'
    body = "Python 邮件发送测试..."
    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ['yu_zhi_peng@126.com'] # 接受邮件
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.126.com", 465, context=context) as smtpObj:
        # 连接成功用，用login登录自己的邮箱和密码
        smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtpObj.send_message(msg)


TC_sendEmail()