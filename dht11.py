import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import requests 

API_KEY         = '79LHF0RNGFQNHVNG'
API_URL         = 'https://api.thingspeak.com/update?api_key=79LHF0RNGFQNHVNG&field1=0'
SLEEP           = 0.01

def initialize_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

def get_data_from_raspberry():
    
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11,4)
       	print("Temperature: %d C" % temperature)
        print("Humidity: %d %%" % humidity)
        send_data_to_thingspeak(temperature, humidity)
        time.sleep(0.1)

def send_data_to_thingspeak(temperature, humidity):     
    data = {'api_key': API_KEY, 'field1':temperature, 'field2':humidity};
    result = requests.post(API_URL, params=data)
    print result.status_code
    if result.status_code == 200:
        print "Success!! Thingspeak"
    else:
        print "Fail!! Thingspeak"

if __name__ == "__main__":
    initialize_GPIO()
    get_data_from_raspberry()
