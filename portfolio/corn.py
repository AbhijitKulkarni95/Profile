import requests
import time
def my_scheduled_job():
    time.sleep(2000)
    requests.get('https://abhijitkulkarni.herokuapp.com/')
    return my_scheduled_job