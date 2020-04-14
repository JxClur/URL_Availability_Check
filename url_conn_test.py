import requests
from collections import namedtuple

urls = []
with open("urls_test_conn.txt") as f:
    content = f.read().splitlines()
    urls.append(content)
    print(urls)

def get_status(site):
    try:
        response = requests.head(site, TimeoutError=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    return

for url in urls:
    website_status = get_status(url)
    print()
        