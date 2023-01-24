import schedule
import server_status
import time


def job_monitor():
    url = "www.google.com"
    server_status.execute_monitor(url)
schedule.every(10).seconds.do(job_monitor)
while True:
    schedule.run_pending()
    time.sleep(1)
