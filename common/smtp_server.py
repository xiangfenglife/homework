# -*- coding:utf-8 -*-

from smtpd import SMTPServer
import asyncore


class CustomSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, mailto, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', mailto
        print 'Message length        :', len(data)
        inheaders = 1
        lines = data.split('\n')
        print '---------- MESSAGE FOLLOWS ----------'
        for line in lines:
            # headers first
            if inheaders and not line:
                print 'X-Peer:', peer[0]
                inheaders = 0
            print line
        print '------------ END MESSAGE ------------'
        return


if __name__ == "__main__":
    server = CustomSMTPServer(('127.0.0.1', 25), None)
    asyncore.loop()