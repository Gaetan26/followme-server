
import time, json, os
from fastapi import FastAPI
from model import PositionData, TakingOffData, LandingData
from mqtt import client as mqtt_client
from mqtt import MQTT_BROKER, MQTT_PORT


app = FastAPI()

@app.get("/")
def index():
    return { "hello": "world" }

@app.post("/follow")
def set_position(data: PositionData):
    position = { "lat": data.lat, "lng": data.lng }

    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=2)
    mqtt_client.loop_start()
    mqtt_client.publish(data.topic, json.dumps(position))
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
    return {
        "topic": data.topic,
        "position": position
    }

@app.post("/takeoff")
def set_takeoff(data: TakingOffData):
    topic = data.topic + "/takeoff"
    
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=2)
    mqtt_client.loop_start()
    mqtt_client.publish(topic, True)
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
    return {
        "topic": data.topic,
        "takeoff": True
    }

@app.post("/landing")
def set_landing(data: LandingData):
    topic = data.topic + "/landing"

    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=2)
    mqtt_client.loop_start()
    mqtt_client.publish(topic, True)
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
    return {
        "topic": data.topic,
        "landing": True
    }
