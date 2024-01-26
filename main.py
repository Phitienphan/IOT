import sys
from Adafruit_IO import MQTTClient
import time
import random

AIO_FEED_ID = ["nutnhan1","nutnhan2"]#nhận dữ liệu từ kênh nào thì khai báo
AIO_USERNAME = "tienhcmut"
AIO_KEY = "aio_CGBk34fBISnRfvnggl2TojBV4Vwx"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload+", feed_id: " + feed_id)

#tạo ra objiect
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected #khai báo 1 conback
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background() 

counter = 1

while True:
    counter = counter -1
    if counter<=0:
        counter=1

        #TODO
        print("random data is publising...")
        temp= random.randint(10,20)
        client.publish("cambien1",temp)
        humi= random.randint(50,70)
        client.publish("cambien2",humi)
        light= random.randint(100,500)
        client.publish("cambien3",light)

    time.sleep(1)
    pass