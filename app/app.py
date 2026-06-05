
import time, json, os
from fastapi import FastAPI
from model import PositionData
from mqtt import client as mqtt_client
from mqtt import MQTT_BROKER, MQTT_PORT


app = FastAPI()

@app.get("/")
def index():
    return { "hello": "world" }

@app.post("/set")
def set_position(data: PositionData):
    position = { "lat": data.lat, "lng": data.lng }

    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=5)
    mqtt_client.loop_start()
    mqtt_client.publish(data.topic, json.dumps(position))
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
    return {
        "topic": data.topic,
        "position": position
    }
