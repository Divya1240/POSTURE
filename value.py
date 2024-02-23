import streamlit as st
import socket

# Function to receive data from ESP32
def receive_data(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            st.write('Connected to:', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                flex_sensor_values = data.decode('utf-8').split(',')
                return flex_sensor_values

def main():
    st.title("Flex Sensor Values Display")

    host = 'your_esp32_ip_address'
    port = 12345  # Choose a port that is not currently in use

    flex_sensor_values = receive_data(host, port)

    if flex_sensor_values:
        st.write("Flex Sensor 1 Value:", flex_sensor_values[0])
        st.write("Flex Sensor 2 Value:", flex_sensor_values[1])
        # Add more lines to display additional flex sensor values if needed

if __name__ == "__main__":
    main()
