# -*- coding:utf-8 -*-

import dns.resolver


def dns_xm(domain):
    MX_info = []
    MX = dns.resolver.query(domain, 'MX')

    if len(MX) != 0:
        for info in MX:
            MX_info.append(info)
            print info
        return MX
    else:
        print "couldn't get MX for %s"%domain


if __name__ == "__main__":

    dns_xm('sina.com')
