import random
import time

from paho.mqtt import client as mqtt_client

# From EMQX tutorial

TCP_PORT = 1883
WEBSOCKET_PORT = 8083
TLS_PORT= 8883
SECURE_WEBSOC_PORT = 8084

# Test using TCP
port = TCP_PORT
broker = 'broker.emqx.io'
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

# Function to connect to MQTT broker
def connect_mqtt():
    def on_connect(client, data, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker.\n")
        else:
            print(f'Failed to connect to MQTT broker. Code: {rc}\n')
    
    # Set connecting client ID
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Publish message to the broker
def publish(client):
    msg_count = 1
    while True:
        time.sleep(1) # pause between messages
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()