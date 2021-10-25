# Import standard python modules
import time
import json
from random import randint

from Adafruit_IO import MQTTClient, Feed, RequestError

ADAFRUIT_IO_KEY = 'aio_aaXQ56Mtv3RWWwps1wWDPCWdq8S6'

ADAFRUIT_IO_USERNAME = 'CSE_BBC1'

aio = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
aio.connect()
# data set up

def publish_ada(data, client=aio, feed='bk-iot-relay'):
    data = json.dumps(data)
    client.publish(feed, data)

    