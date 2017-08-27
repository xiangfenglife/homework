import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from homework.common.dns_fun import dns_xm


def send_mail():

    sender = 'xiangfeng_006@nsb.com'
    receivers = ['1493770186@qq.com']
    cc = ['119912808@qq.com']
    message = MIMEText('python send mail', 'plain', 'utf-8')
    message['from'] = sender
    message['To'] = ','.join(receivers)
    message['Bc'] = ','.join(cc)
    subject = "send Email"
    message['Subject'] = Header(subject, 'utf-8')

    user_addr_dic, domain_xm_dic = get_receivers_xm(receivers + cc)

    for dm1 in user_addr_dic:
        for dm2 in domain_xm_dic:
            if dm1 == dm2:
                mail_server_xm = domain_xm_dic[dm2]
                receivers_lst = user_addr_dic[dm1]
                print mail_server_xm
                print receivers_lst
                smtpobj = smtplib.SMTP(mail_server_xm)
                smtpobj.set_debuglevel(1)
                smtpobj.sendmail(sender, receivers_lst, message.as_string())
                print "send pass"



def get_receivers_xm(addr_lst):

    domain_useraddr_dic={}
    domain_xm_dic = {}
    domain_lst = []
    for addr in addr_lst:
        mail_addr = [addr]
        if "@" in addr:
            domain = addr.split('@')[-1]
            domain_lst.append(domain)
            if domain_useraddr_dic.has_key(domain):
                domain_useraddr_dic[domain].extend(mail_addr)
            else:
                domain_useraddr_dic[domain] = mail_addr

    for domain in set(domain_lst):
        #xm = random.choice(dns_xm(domain)).exchange
        xm = dns_xm(domain)[2].exchange
        domain_xm_dic[domain] = str(xm)[:-1]

    return domain_useraddr_dic, domain_xm_dic


if __name__ == "__main__":

    send_mail()

