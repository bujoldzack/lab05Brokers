import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connect with result code {rc}")
    
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

for i in range(5):
    client.publish('raspberry/zacharie/counter', payload=i, qos=0, retain=False)
    print(f"send {i} to raspberry/zacharie/counter")
    time.sleep(1)

client.loop_forever()
