import streamlit as st
import requests
import json

# Function to fetch data from ThingSpeak
def fetch_data():
    url = 'https://api.thingspeak.com/channels/2203635/feeds.json?api_key=YOUR_API_KEY&results=1'
    response = requests.get(url)
    data = json.loads(response.content)
    return data['feeds'][0] if 'feeds' in data and len(data['feeds']) > 0 else None

def main():
    st.title('Posture Management System')

    # Fetch data from ThingSpeak
    data = fetch_data()
    
    if data:
        posture_angle = float(data.get('field1'))
        # Display posture angle
        st.write(f"Current posture angle: {posture_angle}")

        # Add condition to check posture and display appropriate message
        if abs(posture_angle) > 30:
            st.error("Poor posture detected! Please correct your posture.")
        else:
            st.success("Good posture!")
    else:
        st.error("Failed to fetch data from ThingSpeak. Check your connection or try again later.")

if __name__ == "__main__":
    main()

