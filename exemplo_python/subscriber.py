import paho.mqtt.client as paho
import time

broker = "127.0.0.1"
port = 1883

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print("Publishing message to topic","house/bulb1")

print("creating new instance")
client = paho.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker, port) #connect to broker
print("Subscribing to topic","house/bulb1")
client.subscribe("house/bulb1")
client.loop_forever() #start the loop

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
