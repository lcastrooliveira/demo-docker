# http://www.steves-internet-guide.com/publishing-messages-mqtt-client/

import paho.mqtt.client as paho

broker = "127.0.0.1"
port = 1883

def on_publish(client, userdata, result):
    print("data published \n")
    print(f'published result: {result} on client {client}')

def on_disconnect(client, userdata, rc):
    print("client disconected ok")

client1 = paho.Client("control1")
client1.on_publish = on_publish
client1.on_disconnect = on_disconnect
client1.connect(broker, port)
ret = client1.publish("house/bulb1", "hey hello")
client1.disconnect()