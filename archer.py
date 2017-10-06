#!/usr/bin/python3

import requests
import ssl
import urllib

URL = 'https://superchillin.net/'
HREF = 'href="/dl/42/'

# I think this is a static link
LINK = 'dl/42/842509795e783ee3ec6491102/'

def main():
    with open('cookie') as f:
        cookie = f.read().strip()


    print(get_dl_url(5000, cookie))

def get_dl_url(movie_id, cookie):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(URL + '?' + str(movie_id))
    req.add_header('Cookie', cookie)
    res = urllib.request.urlopen(req, context=ctx)

    body = res.read().decode('utf-8');

    start = body.index("href='/dl/42/")
    end = body.index(".mp4", start)

    return body[start+6:end+4]

if __name__ == '__main__':
    main()
