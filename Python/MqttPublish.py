# coding: utf-8
import sys, os, time
reload(sys)
sys.setdefaultencoding('utf-8')

import paho.mqtt.client as mqtt

# If broker asks client ID.
client_id = "uid1"

client = mqtt.Client(client_id=client_id)

# If broker asks user/password.
user = ""
password = ""
client.username_pw_set(user, password)

client.connect("localhost")

topic = "tw/rocksaying"
payload = "你好 mqtt"

for i in xrange(10):
    client.publish(topic, "%s - %d" % (payload, i))
    time.sleep(0.01)
    # 當 qos = 0, 若訊息間隔太短，就可能會漏發訊息。這是正常現象。