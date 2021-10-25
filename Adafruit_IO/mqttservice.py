# Import standard python modules.
import sys
import json
from Adafruit_IO import MQTTClient, Client
from publish import publish_ada

ADAFRUIT_IO_KEY = 'aio_aaXQ56Mtv3RWWwps1wWDPCWdq8S6'

ADAFRUIT_IO_USERNAME = 'CSE_BBC1'


def connected(client):
    print('Connected!!!')
    client.subscribe()


def message():
    data1 = {"id":"11", "name":"Relay", "data":"0", "unit":""}
    client.publish_ada(data1)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.connect()
