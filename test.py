import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://plmiter.ddns.net/accounts/login?next=/')
if r.status != 200:
    print r.status
    print "something is wrong"
print r.status
print type(r.status)