import random

from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io' # tutorial broker
broker = 'localhost' # running a local Moquitto instance
port = 1883 # TCP port
topic = "python/mqtt"
# Generate a Client ID with a subscribe prefix
client_id = f'subscribe-{random.randint(0, 100)}'

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

# Function to subscribe to MQTT broker
def subscribe(client: mqtt_client):
    def on_message(client, data, message):
         print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
