# -*- coding:utf-8 -*-

from smtpd import SMTPServer
import asyncore


class CustomSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, mailto, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', mailto
        print 'Message length        :', len(data)
        return


if __name__ == "__main__":
    server = CustomSMTPServer(('127.0.0.1', 25), None)
    asyncore.loop()