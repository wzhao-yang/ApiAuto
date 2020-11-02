# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.qq.com"
    send_user = "查看测试笔记"  # 账号
    password = "查看测试笔记"  # 密码

    def send_mail(self, user_list, sub, content):
        user = "zhaoyang" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 统计百分百，浮点型，小数点后两位百分之百
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        user_list = ['zhaoyang.wang@pintec.com']
        sub = "接口自动化测试报告"
        content = "您好:\n\n  总运行接口case数：%d个；\n  通过case数：%d个；\n  失败case数：%d；\n  通过率：%s；\n  失败率：%s" % (
            count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1, 2, 3], [1, 2, 3, 4, 5, 6, 7])
    # sen.send_main()
