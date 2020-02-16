#!/usr/bin/env python

import OpenSSL.crypto as crypto
import click
import socket
import ssl

from datetime import datetime
from prettytable import PrettyTable


pt = PrettyTable()
pt.field_names = [
    "Host",
    "Common Name",
    "NotBefore",
    "NotAfter",
    "Issuer",
]
pt.align = "l"


def expiration_check(target: str) -> None:
    ctx = ssl.create_default_context()
    conn = ctx.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=target,
    )

    conn.settimeout(1.0)
    conn.connect((target, 443))

    cert_info = conn.getpeercert(True)

    x509 = crypto.load_certificate(
        crypto.FILETYPE_ASN1,
        cert_info
    )

    pt.add_row([
        target,
        x509.get_subject().CN,
        datetime.strptime(
            x509.get_notBefore().decode('ascii'),
            '%Y%m%d%H%M%SZ'
        ),
        datetime.strptime(
            x509.get_notAfter().decode('ascii'),
            '%Y%m%d%H%M%SZ'
        ),
        x509.get_issuer().CN,
    ])


@click.command()
@click.option('-H', '--hosts', help='target hosts, splits by comma')
def check(hosts):
    for host in hosts.split(','):
        expiration_check(host)

    print(pt.get_string(sortby="NotAfter", reversesort=False))


if __name__ == '__main__':
    check()
