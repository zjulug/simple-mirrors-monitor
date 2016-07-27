__author__ = 'vxst'
import smtplib
from email.mime.text import MIMEText


def alert(dist, information):
    with open('.password', 'r') as f:
        password = f.read().split()[0]
    with open('.site', 'r') as f:
        site = f.read().split()[0]
    information = "The alert for dist {} has happened:\n{}".format(dist, information)

    fromAddress = "zju-mirrors-alert@vxst.org"
    toAddress = "vxst@vxst.org"

    msg = MIMEText(information)
    msg['Subject'] = "Alert From ZJU Mirrors"
    msg["From"] = fromAddress
    msg["To"] = toAddress

    smtp = smtplib.SMTP(site)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(fromAddress, password)
    smtp.sendmail(fromAddress, [toAddress, ], msg.as_string())
    smtp.quit()
