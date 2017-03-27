#!flask/bin/python

import requests
import sys

if len(sys.argv) != 3:
    print("USAGE: python client.py <IP> <port>")
    sys.exit(0)

ip = sys.argv[1]
port = sys.argv[2]

req = "http://%s:%s/stats/counter" % (ip, port)
resp = requests.get(req)
if resp.status_code != 200:
    # Error
    raise ApiError("GET %s: resp status %d" % (req, resp.status_code))

print ("RESPONSE: %s" % repr(resp.json()))
