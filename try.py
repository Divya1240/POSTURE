import streamlit as st
import requests
import time
from Adafruit_ADS1x15 import ADS1x15
from mpu6050 import mpu6050

# Initialize Flex Sensor and Accelerometer
adc = ADS1x15(ic=ADS1x15.IC_ADS1015)
sensor = mpu6050(0x68)

# ThingSpeak Configuration
WRITE_API_KEY = 'VRIE177CD367T7YR'
READ_API_KEY = 'RLO328KCGVSX1VTR'
CHANNEL_ID = '2442448'

def read_flex_sensor():
    # Read flex sensor value
    flex_value = adc.read_adc(0, gain=1)
    return flex_value

def read_accelerometer():
    # Read accelerometer data
    accel_data = sensor.get_accel_data()
    return accel_data['x'], accel_data['y'], accel_data['z']

def send_to_thingspeak(flex_value, x_accel, y_accel, z_accel):
    # Send data to ThingSpeak
    url = f'https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field1={flex_value}&field2={x_accel}&field3={y_accel}&field4={z_accel}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully")
    else:
        print("Failed to send data to ThingSpeak")

def fetch_data_from_thingspeak():
    # Fetch data from ThingSpeak
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['feeds'][0]
    else:
        return None

def main():
    st.title('Posture Management System')

    while True:
        flex_value = read_flex_sensor()
        x_accel, y_accel, z_accel = read_accelerometer()
        send_to_thingspeak(flex_value, x_accel, y_accel, z_accel)
        time.sleep(15)  # Adjust the delay as needed

        st.header('Current Data from ThingSpeak')
        data = fetch_data_from_thingspeak()
        if data:
            st.write('Flex Sensor Value:', data['field1'])
            st.write('X Acceleration:', data['field2'])
            st.write('Y Acceleration:', data['field3'])
            st.write('Z Acceleration:', data['field4'])
        else:
            st.write('Failed to fetch data from ThingSpeak')

if __name__ == "__main__":
    main()


