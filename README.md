# SSL certificate checker written in python

## Prerequisites

Setup requirements

    $ pip install -r requirements.txt

## Examples

check single target host certificates infomation

    $ ./ssl-certs-checker.py --hosts "www.google.com"

    +----------------+----------------+---------------------+---------------------+------------+
    | Host           | Common Name    | NotBefore           | NotAfter            | Issuer     |
    +----------------+----------------+---------------------+---------------------+------------+
    | www.google.com | www.google.com | 2020-02-12 11:47:41 | 2020-05-06 11:47:41 | GTS CA 1O1 |
    +----------------+----------------+---------------------+---------------------+------------+

check multiple target hosts' certificates at once

    $ ./ssl-certs-checker.py --hosts "www.google.com,www.azure.com,www.amazon.com"

    +----------------+----------------+---------------------+---------------------+-----------------------+
    | Host           | Common Name    | NotBefore           | NotAfter            | Issuer                |
    +----------------+----------------+---------------------+---------------------+-----------------------+
    | www.google.com | www.google.com | 2020-02-12 11:47:41 | 2020-05-06 11:47:41 | GTS CA 1O1            |
    | www.amazon.com | www.amazon.com | 2019-09-18 00:00:00 | 2020-08-23 12:00:00 | DigiCert Global CA G2 |
    | www.azure.com  | *.azure.com    | 2019-12-17 19:51:44 | 2020-12-17 19:51:44 | Microsoft IT TLS CA 4 |
    +----------------+----------------+---------------------+---------------------+-----------------------+

# License

[MIT LICENSE](LICENSE)
