class Nodemcu:
    def __init__(self):
        import paho.mqtt.client as mqtt
        self.broker_address = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.mqtt = mqtt


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        #print(msg.topic+" "+str(msg.payload))
        print(msg.payload)

    def connect(self):
        self.client = self.mqtt.Client()
        self.client.username_pw_set(self.user, password=self.password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker_address, port=self.port)
        print(self.port)
        self.client.subscribe("/nodemcu_1/")
        self.client.loop_forever()

test = Nodemcu()
test.broker_address = "192"
test.port = 1883
test.user = "nodemcu"
test.password = ""

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
