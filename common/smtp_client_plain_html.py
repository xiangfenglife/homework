import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from homework.common.dns_fun import dns_xm


def send_mail_plain_html(sender, receivers, subject, body, cc=None, bcc=None, ):
    message = MIMEText(body, 'plain', 'utf-8')
    message['from'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header(subject, 'utf-8')

    if cc:
        message['Cc'] = ','.join(cc)
        receivers.extend(cc)
    if bcc:
        message['bCc'] = ','.join(bcc)
        receivers.extend(bcc)

    user_addr_dic, domain_xm_dic = get_receivers_xm(receivers)

    for dm1 in user_addr_dic:
        for dm2 in domain_xm_dic:
            if dm1 == dm2:
                mail_server_xm = domain_xm_dic[dm2]
                receivers_lst = user_addr_dic[dm1]
                print mail_server_xm
                #print receivers_lst
                try:
                    smtpobj = smtplib.SMTP(mail_server_xm)
                    smtpobj.set_debuglevel(0)
                    smtpobj.sendmail(sender, receivers_lst, message.as_string())
                    print "send the mail to %s complete" % ','.join(receivers_lst)
                except:
                    print mail_server_xm
                    print "send the mail to %s failure" % ','.join(receivers_lst)


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
        domain_xm_dic[domain] = dns_xm(domain)

    return domain_useraddr_dic, domain_xm_dic


if __name__ == "__main__":
    sender = 'xiangfeng_006@nsb.com'
    receivers = ['xiangfeng_006@sina.com']
    cc = ['119912808@qq.com']
    subject = "send Email"
    body = 'python --SMTP send Email'
    send_mail_plain_html(sender=sender,receivers=receivers,subject=subject,body=body)

