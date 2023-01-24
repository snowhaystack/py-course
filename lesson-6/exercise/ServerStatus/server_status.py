import subprocess,re,requests
from pprint import pprint
from functools import reduce
import send_alert


def execute_ping(check_url):
    result_host = (False,0)
    result_p = subprocess.run(['ping',check_url], capture_output=True, text=True)
    out = result_p.stdout.split("\n")
    result = list(filter(lambda val: val.startswith("Reply"), out))
    if len(result)>0:
        search_pattern = re.compile("time=(\d+)ms")
        time_ms = [int(search_pattern.search(val).group(1)) for val in result]
        avarage_ms = round(reduce(lambda a,b: a+b, time_ms)/len(time_ms),2)
        result_host = (True, avarage_ms)
    return result_host

def get_ipaddress():
    url_api = "https://ipinfo.io"
    response = requests.get(url_api)
    return response
def execute_monitor(url):
    result_monitor = execute_ping(url)
    pprint(result_monitor)
    ip_address = get_ipaddress()
    pprint(ip_address)
    send_alert.send_email(ip_address, result_monitor[0], result_monitor[1], "pythonfrom0tohero@gmail.com")

#https://regexr.com/
#https://regex101.com/
#https://rubular.com/r/DHt8RHjWYH
if __name__ == '__main__':
    check_url = 'google.com'
    #check_url = 'wsbot.eu'
    ip_address = get_ipaddress().json()['ip']
    pprint(f'ip => {ip_address}')
    result_monitor = execute_ping(check_url)
    pprint(f'monitoring => {result_monitor}')
    send_alert.send_email(ip_address, result_monitor[0], result_monitor[1], "tiaf9640@gmail.com")
