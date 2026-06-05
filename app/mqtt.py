
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import os

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER") 
MQTT_PORT = int(os.getenv("MQTT_PORT")) 

client = mqtt.Client(
    callback_api_version = mqtt.CallbackAPIVersion.VERSION2
)
